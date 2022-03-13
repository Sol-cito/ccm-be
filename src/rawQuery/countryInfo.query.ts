export const TemperatureByAlpha3Code = (alpha3Code: string) => {
  const query =
    'SELECT ' +
    'year_1901, year_1902, year_1903, year_1904, year_1905, year_1906, year_1907, year_1908, year_1909, year_1910, year_1911, year_1912, year_1913, year_1914, year_1915, year_1916, year_1917, year_1918, year_1919, year_1920, year_1921, year_1922, year_1923, year_1924, year_1925, year_1926, year_1927, year_1928, year_1929, year_1930, year_1931, year_1932, year_1933, year_1934, year_1935, year_1936, year_1937, year_1938, year_1939, year_1940, year_1941, year_1942, year_1943, year_1944, year_1945, year_1946, year_1947, year_1948, year_1949, year_1950, year_1951, year_1952, year_1953, year_1954, year_1955, year_1956, year_1957, year_1958, year_1959, year_1960, year_1961, year_1962, year_1963, year_1964, year_1965, year_1966, year_1967, year_1968, year_1969, year_1970, year_1971, year_1972, year_1973, year_1974, year_1975, year_1976, year_1977, year_1978, year_1979, year_1980, year_1981, year_1982, year_1983, year_1984, year_1985, year_1986, year_1987, year_1988, year_1989, year_1990, year_1991, year_1992, year_1993, year_1994, year_1995, year_1996, year_1997, year_1998, year_1999, year_2000, year_2001, year_2002, year_2003, year_2004, year_2005, year_2006, year_2007, year_2008, year_2009, year_2010, year_2011, year_2012, year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020 ' +
    " FROM country_temperature WHERE alpha3_code = '" +
    alpha3Code +
    "';";
  return query;
};
