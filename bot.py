from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import aiohttp
TOKEN = '5941668474:AAHxfY0HOyM3CSMfXjyAw1yAJkbo5wm6t-Y'
API_ENDPOINT_APPOINTMENT = 'http://127.0.0.1:8000/api/make_appointment'
API_ENDPOINT_CHECK_USER = 'http://127.0.0.1:8000/api/check_user'

API_ENDPOINT_LINK = 'http://127.0.0.1:8000/api/recover'
API_ENDPOINT_PASSWORD = 'http://127.0.0.1:8000/api/send-temp-password'

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Вы можете использовать /send_link для отправки ссылки на сброс пароля или /send_temp_password для получения временного пароля.")


# Создаем состояние для восстановления доступа
class RecoveryForm(StatesGroup):
    contact = State()

@dp.message_handler(commands=['send_link'])
async def send_link(message: types.Message):
    await message.reply("Введите ваш email или номер телефона для восстановления доступа:")
    await RecoveryForm.contact.set()  # Переходим в состояние ожидания ввода контакта

@dp.message_handler(state=RecoveryForm.contact)
async def handle_recovery_contact(message: types.Message, state: FSMContext):
    contact = message.text
    async with aiohttp.ClientSession() as session:
        async with session.post(API_ENDPOINT_LINK, json={'contact': contact}) as response:
            if response.status == 200:
                await message.reply("Инструкции по восстановлению доступа были отправлены.")
            else:
                await message.reply("Произошла ошибка или пользователь не найден.")
    await state.finish()  # Завершаем состояние восстановления доступа

@dp.message_handler(commands=['send_temp_password'])
async def send_temp_password(message: types.Message):
    await message.reply("Отправьте мне ваш email для получения временного пароля.")

@dp.message_handler()
async def handle_temp_password_input(message: types.Message):
    user_input = message.text
    async with aiohttp.ClientSession() as session:
        async with session.post(API_ENDPOINT_PASSWORD, data={'contact': user_input}) as response:
            if response.status == 200:
                data = await response.json()
                temp_password = data.get("temp_password")
                # Предполагается, что сервер возвращает временный пароль и инструкции
                await message.reply(f"Ваш временный пароль: {temp_password}. Пожалуйста, измените его при следующем входе.")
            else:
                await message.reply("Произошла ошибка или пользователь не найден.")

class AppointmentForm(StatesGroup):
    is_registered = State()
    email = State()
    date = State()
    non_registered_patient_name = State()
    non_registered_patient_contact = State()
def get_registration_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton("Да"), KeyboardButton("Нет"))
    return keyboard

@dp.message_handler(commands=['make_appointment'])
async def start_appointment(message: types.Message):
    keyboard = get_registration_keyboard()
    await message.reply("Вы зарегистрированный пользователь на сайте?", reply_markup=keyboard)
    await AppointmentForm.is_registered.set()

@dp.message_handler(lambda message: message.text in ["Да", "Нет"], state=AppointmentForm.is_registered)
async def process_registration(message: types.Message, state: FSMContext):
    if message.text == "Да":
        await message.reply("Введите ваш email для проверки регистрации:")
        await AppointmentForm.email.set()
    else:
        await message.reply("Введите ваше полное имя:")
        await AppointmentForm.non_registered_patient_name.set()

@dp.message_handler(state=AppointmentForm.email)
async def process_email(message: types.Message, state: FSMContext):
    email = message.text.strip()
    is_registered, user_info = await check_user_registration(email)

    if is_registered:
        full_name = user_info.get('full_name') if user_info else "Неизвестный пользователь"
        await state.update_data(registered_user_info=user_info)
        await message.reply(f"Пользователь найден: {full_name}. Введите дату приема (ГГГГ-ММ-ДД):")
        await AppointmentForm.date.set()
    else:
        await message.reply("Электронная почта не найдена. Пожалуйста, попробуйте еще раз.")
        await AppointmentForm.email.set()


@dp.message_handler(state=AppointmentForm.non_registered_patient_name)
async def process_non_registered_name(message: types.Message, state: FSMContext):
    non_registered_name = message.text.strip()
    await state.update_data(non_registered_patient_name=non_registered_name)
    await message.reply("Введите ваш контактный номер:")
    await AppointmentForm.non_registered_patient_contact.set()


@dp.message_handler(state=AppointmentForm.non_registered_patient_contact)
async def process_non_registered_contact(message: types.Message, state: FSMContext):
    non_registered_contact = message.text.strip()
    await state.update_data(non_registered_patient_contact=non_registered_contact)

    user_data = await state.get_data()
    if 'date' not in user_data:
        await message.reply("Введите дату приема (ГГГГ-ММ-ДД):")
        await AppointmentForm.date.set()
    else:
        # Если дата уже введена, завершаем процесс
        await send_appointment_data(message, state)
# Отдельная функция для отправки данных на сервер
async def send_appointment_data(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    # Проверяем, все ли данные доступны для отправки
    if 'non_registered_patient_name' in user_data and 'non_registered_patient_contact' in user_data and 'date' in user_data:
        appointment_data = {
            'non_registered_patient_name': user_data['non_registered_patient_name'],
            'non_registered_patient_contact': user_data['non_registered_patient_contact'],
            'date': user_data['date'],
        }
        response = await make_appointment_on_server(appointment_data)
        await process_response(message, response)
    await state.finish()

async def make_appointment_on_server(appointment_data):
    async with aiohttp.ClientSession() as session:
        async with session.post(API_ENDPOINT_APPOINTMENT, json=appointment_data) as response:
            response_data = await response.json()
            return response_data

async def check_user_registration(email):
    async with aiohttp.ClientSession() as session:
        try:
            response = await session.post(API_ENDPOINT_CHECK_USER, json={'email': email})
            if response.status == 200:
                data = await response.json()
                is_registered = data.get('is_registered', False)
                user_info = data.get('user_info') if is_registered else None
                return is_registered, user_info
        except Exception as e:
            print(f"Error checking user registration: {e}")
    return False, None


@dp.message_handler(state=AppointmentForm.date)
async def process_date(message: types.Message, state: FSMContext):
    date = message.text.strip()
    await state.update_data(date=date)

    user_data = await state.get_data()
    registered_user_info = user_data.get('registered_user_info')

    if registered_user_info:
        # Отправка данных зарегистрированного пользователя
        appointment_data = {
            'date': date,
            'patient_name': registered_user_info.get('id'),
        }
        response = await make_appointment_on_server(appointment_data)
        await process_response(message, response)
        await state.finish()
    else:
        # Продолжение процесса для незарегистрированного пользователя
        # Если все данные (имя, контакт) уже введены, отправляем на сервер
        non_registered_name = user_data.get('non_registered_patient_name')
        non_registered_contact = user_data.get('non_registered_patient_contact')
        if non_registered_name and non_registered_contact:
            await send_appointment_data(message, state)
        else:
            # Если какие-то данные отсутствуют, продолжаем запрашивать их
            if not non_registered_name:
                await message.reply("Введите ваше полное имя:")
                await AppointmentForm.non_registered_patient_name.set()
            elif not non_registered_contact:
                await message.reply("Введите ваш контактный номер:")
                await AppointmentForm.non_registered_patient_contact.set()

@dp.message_handler(state=AppointmentForm.non_registered_patient_contact)
async def process_non_registered_contact(message: types.Message, state: FSMContext):
    non_registered_contact = message.text.strip()
    await state.update_data(non_registered_patient_contact=non_registered_contact)
    await send_appointment_data(message, state)

async def process_response(message, response):
    if response.get('success'):
        await message.reply("Вы успешно записаны на прием.")
    else:
        await message.reply("Произошла ошибка при записи на прием.")


if __name__ == '__main__':
    from aiogram.utils import executor
    executor.start_polling(dp, skip_updates=True)