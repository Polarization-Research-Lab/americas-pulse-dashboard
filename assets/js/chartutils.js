async function pull(source) {
    const response = await fetch(source)
    return response.json()
}

Chart.defaults.font.family = 'Helvetica';









