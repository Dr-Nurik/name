document.addEventListener("DOMContentLoaded", function() {
    var ctx = document.getElementById('gymChart').getContext('2d');
    var gymChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: gymData.labels,
            datasets: [{
                label: 'Тренажерный зал',
                data: gymData.data,
                backgroundColor: ['#FF6384', '#36A2EB'],
                borderColor: ['#FF6384', '#36A2EB'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true
        }
    });
});
