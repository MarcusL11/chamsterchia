
const radar_data = [4,5,7,2,8];
const radar_data_2 = [3,6,9,4,5];

const radar_labels = [
    "Power",
    "Accuracy",
    "Luck",
    "Recovery",
    "Putting",
];

const myChart = new Chart('myChart', {
    type: 'radar',
    data: {
        labels: radar_labels,
        datasets: [
            {
                label: 'Skills',
                data: radar_data,
                fill: true,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgb(255, 99, 132)',
                pointBorderColor: '#fff',
                borderDash: [3, 5],
                tension: 0.2,
            },
            {
                label: 'Average',
                data: radar_data_2,
                fill: true,
                backgroundColor: 'rgba(15, 25, 132, 0.2)',
                borderColor: 'rgb(15, 25, 132)',
                pointBackgroundColor: 'rgb(15, 25, 132)',
                pointBorderColor: '#fff',
                tension: 0.2,
            },            
        ]
    },
    options: {
        elements: {
            line: {
                borderWidth: 2.5
            }
        }
    }
});