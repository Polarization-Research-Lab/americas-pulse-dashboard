function build () {
  const canvasid_affpolhist = document.currentScript.getAttribute('data-canvasid')
  const datasource = document.currentScript.getAttribute('data-source')

  fetch(datasource)
    .then((request) => request.json())
    .then((data) => {
      const canvas = document.getElementById(canvasid_affpolhist)
      const chart = new Chart(
        canvas.getContext('2d'),
        {
          type: 'line',
          data: {
            labels: data.x,
            datasets: [
              {
                label: 'Democrat',
                data: data.Democrat,
                color: 'blue',
                borderColor: 'rgba(19, 105, 235,.9)',
                backgroundColor: 'rgba(19, 105, 235,.9)',
                tension: 0.2,
                borderWidth: 4,
                pointRadius: 0
              },
              {
                label: 'Republican',
                data: data.Republican,
                color: 'red',
                borderColor: 'rgba(247, 5, 33,.9)',
                backgroundColor: 'rgba(247, 5, 33,.9)',
                tension: 0.2,
                borderWidth: 4,
                pointRadius: 0
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: false,
            scales: {
              y: {
                min: 0,
                max: 4,
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
                    switch (label) {
                      case 0:
                        return ['Strongly', 'oppose']
                      case 1:
                        return 'Oppose'
                      case 2:
                        return ['Neither support', 'nor oppose']
                      case 3:
                        return 'Support'
                      case 4:
                        return ['Strongly', 'support']
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
              // zoom: {
              //   pan: {
              //     enabled: true,
              //     mode: 'x',
              //   },
              //   zoom: {
              //     wheel: {
              //       // enabled: true,
              //     },
              //     drag: {enabled: true},
              //     mode: 'x',
              //   },
              //   limits: {
              //     // x: {minRange: },
              //       x: {
              //           min: Date.parse(data['x'][0]),
              //           max: Date.parse(data['x'][data['x'].length - 1]),
              //       },
              //   }
              // },
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
