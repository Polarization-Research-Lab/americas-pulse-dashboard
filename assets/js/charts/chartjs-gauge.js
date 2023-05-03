
function build () {
  const value = document.currentScript.getAttribute('data-gauge')
  const max = document.currentScript.getAttribute('data-max')

  const ctx = document.getElementById(
    document.currentScript.getAttribute('data-canvasid')
  ).getContext('2d')

  const chart = new Chart(
    ctx,
    {
      type: 'doughnut',
      data: {
        labels: [],
        datasets: [{
          label: '# of Votes',
          data: [0, value, max - value],
          backgroundColor: ['Grey', 'Teal']
          // min: 0,
          // max: 100,
        }]
      },
      options: {
        rotation: 270, // start angle in degrees
        circumference: 180, // sweep angle in degrees
        maintainAspectRatio: false,
        plugins: {
          tooltip: {
            enabled: false
          }
        }
      }
    }
  )
}

build()
