document.addEventListener("DOMContentLoaded", function() {
    var backgroundColors = serviceData.labels.map(() => `rgba(${[...Array(3)].map(() => Math.floor(Math.random() * 256)).join(', ')}, 0.2)`);

    var ctx = document.getElementById('serviceChart').getContext('2d');
    var serviceChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: serviceData.labels,
            datasets: [{
                label: 'Услуги',
                data: serviceData.data,
                backgroundColor: backgroundColors,
                borderColor: backgroundColors.map(color => color.replace('0.2', '1')),
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: true
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            var value = serviceData.data[tooltipItem.dataIndex];
                            var total = serviceData.data.reduce((sum, value) => sum + value, 0);
                            var percentage = ((value / total) * 100).toFixed(2);
                            return serviceData.labels[tooltipItem.dataIndex] + ': ' + value + ' (' + percentage + '%)';
                        }
                    }
                }
            }
        }
    });
});
