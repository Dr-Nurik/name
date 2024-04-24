# Generated by Django 5.0 on 2024-04-08 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_remove_reception_date_kz_remove_reception_date_ru_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diagnosis',
            old_name='diagnosis_text_kz',
            new_name='diagnosis_text_kk',
        ),
        migrations.RenameField(
            model_name='diagnosis',
            old_name='treatment_text_kz',
            new_name='treatment_text_kk',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='bio_kz',
            new_name='bio_kk',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='doctors_name_kz',
            new_name='doctors_name_kk',
        ),
        migrations.RenameField(
            model_name='equipmentservicehistory',
            old_name='description_kz',
            new_name='description_kk',
        ),
        migrations.RenameField(
            model_name='masseur',
            old_name='bio_kz',
            new_name='bio_kk',
        ),
        migrations.RenameField(
            model_name='masseur',
            old_name='masseur_name_kz',
            new_name='masseur_name_kk',
        ),
        migrations.RenameField(
            model_name='medicalequipment',
            old_name='description_kz',
            new_name='description_kk',
        ),
        migrations.RenameField(
            model_name='medicalequipment',
            old_name='name_kz',
            new_name='name_kk',
        ),
        migrations.RenameField(
            model_name='reception',
            old_name='comed_kz',
            new_name='comed_kk',
        ),
        migrations.RenameField(
            model_name='reception',
            old_name='declined_kz',
            new_name='declined_kk',
        ),
        migrations.RenameField(
            model_name='reception',
            old_name='fullname_patient_kz',
            new_name='fullname_patient_kk',
        ),
        migrations.RenameField(
            model_name='reception',
            old_name='is_confirmed_kz',
            new_name='is_confirmed_kk',
        ),
        migrations.RenameField(
            model_name='reception',
            old_name='no_show_kz',
            new_name='no_show_kk',
        ),
        migrations.RenameField(
            model_name='reception',
            old_name='patient_contact_kz',
            new_name='patient_contact_kk',
        ),
        migrations.RenameField(
            model_name='reception',
            old_name='payment_confirmed_kz',
            new_name='payment_confirmed_kk',
        ),
        migrations.RenameField(
            model_name='reception',
            old_name='requires_massage_kz',
            new_name='requires_massage_kk',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='about_kz',
            new_name='about_kk',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='name_kz',
            new_name='name_kk',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='price_kz',
            new_name='price_kk',
        ),
        migrations.RenameField(
            model_name='specializationcategory',
            old_name='name_kz',
            new_name='name_kk',
        ),
        migrations.RenameField(
            model_name='trainer',
            old_name='bio_kz',
            new_name='bio_kk',
        ),
        migrations.RenameField(
            model_name='trainer',
            old_name='trainer_name_kz',
            new_name='trainer_name_kk',
        ),
        migrations.RenameField(
            model_name='trainingequipment',
            old_name='description_kz',
            new_name='description_kk',
        ),
        migrations.RenameField(
            model_name='trainingequipment',
            old_name='name_kz',
            new_name='name_kk',
        ),
    ]