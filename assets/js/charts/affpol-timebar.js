function build () {
  const canvas = document.getElementById(
    document.currentScript.getAttribute('data-canvasid')
  )
  const yticks = [0, 20, 40, 60, 80, 100]
  const chart = new Chart(
    canvas.getContext('2d'),
    {
      type: 'bar',
      data: {
        labels: ['2 weeks ago', 'Last week', 'This week'],
        datasets: [{
          data: [
            parseInt(document.currentScript.getAttribute('data-2weeksago')),
            parseInt(document.currentScript.getAttribute('data-lastweek')),
            parseInt(document.currentScript.getAttribute('data-thisweek'))
          ],
          backgroundColor: 'rgba(119, 0, 255,.7)',
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: false,
        plugins: {
          legend: {
            display: false
          },
          title: {
            display: true, text: 'Past 3 Weeks:'
          }
        },
        scales: {
          y: {
            min: 0,
            max: 100,
            grid: { display: false },
            ticks: {
              callback: function (value, index, ticks) {
                if (yticks.includes(value)) {
                  return value
                }
              }
            }
          },
          x: {
            grid: { display: false }
          }
        }
      }
    }
  )
}

build()
