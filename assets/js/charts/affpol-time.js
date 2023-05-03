const canvasid_affpoltime = document.currentScript.getAttribute('data-canvasid')

fetch('/americas-pulse-dashboard/assets/data/affpol-time.json')
  .then((request) => request.json())
  .then((data) => {
    canvas = document.getElementById(canvasid_affpoltime)
    const yticks = [0, 20, 40, 60, 80, 100]
    const chart = new Chart(
      canvas.getContext('2d'),
      {
        type: 'line',
        data: {
          labels: data.Democrat.x,
          datasets: [
            {
              label: 'Dem',
              data: data.Democrat.y_weighted,
              color: 'blue',
              borderColor: 'rgba(19, 105, 235,.9)',
              backgroundColor: 'rgba(19, 105, 235,.9)',
              tension: 0.2,
              borderWidth: 4,
              pointRadius: 0
            },
            {
              label: 'Rep',
              data: data.Republican.y_weighted,
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
              max: 100,
              grid: { display: false },
              ticks: {
                font: {
                  weight: 'bold',
                  size: 15,
                  color: 'rgba(0,0,0,1)'
                },

                callback: function (value, index, ticks) {
                  if (yticks.includes(value)) {
                    return value
                  }
                }
                // tickWidth: 100,
                // tickLength
                // lineWidth:
              },
              title: {
                display: true,
                text: 'Polarization',
                font: { size: 25 }
              }
            },
            x: {
              grid: { display: false },
              type: 'time',
              time: {
                unit: 'month'
              },
              ticks: {
                minRotation: 45,
                font: {
                  weight: 'bold',
                  size: 15,
                  color: 'rgba(0,0,0,1)'
                }
              }
            }

          },
          plugins: {
            zoom: {
              pan: {
                enabled: true,
                mode: 'x'
              },
              zoom: {
                wheel: {
                  // enabled: true
                },
                mode: 'x'
              },
              limits: {
                // x: {minRange: },
                x: {
                  min: Date.parse(data.Democrat.x[0]),
                  max: Date.parse(data.Democrat.x[data.Democrat.x.length - 1])
                }
              }
            },
            legend: {
              display: true,
              position: 'right',
              labels: {
                font: {
                  size: 20,
                  weight: 'bold'
                }
              }
            }
          }
        }
      }
    )

    canvas.addEventListener('click', function () {
  	console.log('clicked')
    })
  })
