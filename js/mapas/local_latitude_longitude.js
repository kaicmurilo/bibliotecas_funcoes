/**
 * Async function to fetch location data from OpenStreetMap API based on latitude and longitude.
 *
 * @param {number} latitude - The latitude coordinate.
 * @param {number} longitude - The longitude coordinate.
 * @return {object} An object containing the city, state, and country based on the provided latitude and longitude.
 */
async function buscarLocalizacaoOSM(latitude, longitude) {
  const url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`;

  try {
    const response = await fetch(url, {
      headers: { "User-Agent": "NomeDoSeuApp/versao" },
    });
    const data = await response.json();

    if (data.address) {
      const cidade =
        data.address.city || data.address.town || data.address.village;
      const estado = data.address.state;
      const pais = data.address.country;

      return { cidade, estado, pais };
    }
    return null;
  } catch (error) {
    console.error("Erro ao buscar localização pelo OSM:", error);
    return null;
  }
}

buscarLocalizacaoOSM(-15.13, -53.19)
  .then((localizacao) => console.log(localizacao))
  .catch((error) => console.error(error));
