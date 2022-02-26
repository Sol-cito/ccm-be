export const TemperatureByAlpha3Code = (alpha3Code: string) => {
  const query =
    "SELECT * FROM country_temperature WHERE alpha3_code = '" +
    alpha3Code +
    "';";
  return query;
};
