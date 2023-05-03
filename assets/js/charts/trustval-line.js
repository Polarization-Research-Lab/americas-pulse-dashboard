function build () {
  const canvasid = document.currentScript.getAttribute('data-canvasid')
  const datasource = document.currentScript.getAttribute('data-source')

  const yscale_labels = {
    0: document.currentScript.getAttribute('data-ylabel-0'),
    1: document.currentScript.getAttribute('data-ylabel-1'),
    2: document.currentScript.getAttribute('data-ylabel-2'),
    3: document.currentScript.getAttribute('data-ylabel-3'),
    4: document.currentScript.getAttribute('data-ylabel-4')
  }

  fetch(datasource)
    .then((request) => request.json())
    .then((data) => {
      const canvas = document.getElementById(canvasid)
      const chart = new Chart(
        canvas.getContext('2d'),
        {
          type: 'line',
          data: {
            labels: data.x,
            datasets: [
              {
                label: 'Democrats',
                data: data.Democrats,
                color: 'blue',
                borderColor: 'rgba(19, 105, 235,.9)',
                backgroundColor: 'rgba(19, 105, 235,.9)',
                tension: 0.2,
                borderWidth: 4,
                pointRadius: 0
              },
              {
                label: 'Republicans',
                data: data.Republicans,
                color: 'red',
                borderColor: 'rgba(247, 5, 33,.9)',
                backgroundColor: 'rgba(247, 5, 33,.9)',
                tension: 0.2,
                borderWidth: 4,
                pointRadius: 0
              },
              {
                label: 'Independents',
                data: data.Independents,
                color: 'purple',
                borderColor: 'rgba(131, 52, 235, .9)',
                backgroundColor: 'rgba(131, 52, 235, .9)',
                tension: 0.2,
                borderWidth: 4,
                pointRadius: 0
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            // animation: false,
            scales: {
              y: {
                min: 1,
                max: 5,
                grid: { display: false },
                ticks: {
                  font: {
                    weight: 'bold',
                    size: 15,
                    color: 'rgba(0,0,0,1)'
                  },
                  count: 5,
                  // minRotation: 35,
                  callback: function (label, index, labels) {
                    switch (index) {
                      case 4:
                        return eval(yscale_labels[4])
                      case 3:
                        return eval(yscale_labels[3])
                      case 2:
                        return eval(yscale_labels[2])
                      case 1:
                        return eval(yscale_labels[1])
                      case 0:
                        return eval(yscale_labels[0])
                    }
                  }
                  // function(value, index, ticks) {
                  // if (yticks.includes(value)) {
                  // return value;
                  // }
                  // },
                  // tickWidth: 100,
                  // tickLength
                  // lineWidth:
                }
              },
              x: {
                grid: { display: false },
                type: 'time',
                time: {
                  unit: 'month'
                },
                ticks: {
                  // minRotation: 15,
                  font: {
                    weight: 'bold',
                    size: 15,
                    color: 'rgba(0,0,0,1)'
                  }
                }
              }
            },
            plugins: {
              legend: {
                display: true,
                position: 'bottom',
                labels: {
                  font: {
                    size: 12,
                    weight: 'bold'
                  }
                }
              }
            }
          }
        }
      )
    })
}

build()
