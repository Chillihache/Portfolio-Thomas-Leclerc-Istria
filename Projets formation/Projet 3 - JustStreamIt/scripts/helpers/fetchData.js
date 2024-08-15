export async function fetchData(url) {
    try {
      const response = await fetch(url)
      if (!response.ok) {
        throw new Error(response.statusText)
      }
      const jsonData = await response.json()
      return jsonData;
    } catch (error) {
        console.error("Erreur fetch: " + error)
    }
  }