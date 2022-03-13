import requests
import Common

BASE_URL = "https://climatedata.worldbank.org/ClimateAPIWeb/rest/v2/crunew/cru-ts4.05-timeseries/tas/annual/timeseries/1901-2020/country/"

ALPHA3CODE_LIST = ['AFG', 'ALA', 'ALB', 'DZA', 'ASM', 'AND', 'AGO', 'AIA', 'ATA', 'ATG', 'ARG', 'ARM', 'ABW', 'AUS',
                   'AUT', 'AZE', 'BHS', 'BHR', 'BGD', 'BRB', 'BLR', 'BEL', 'BLZ', 'BEN', 'BMU', 'BTN', 'BOL', 'BES',
                   'BIH', 'BWA', 'BVT', 'BRA', 'IOT', 'BRN', 'BGR', 'BFA', 'BDI', 'CPV', 'KHM', 'CMR', 'CAN', 'CYM',
                   'CAF', 'TCD', 'CHL', 'CHN', 'CXR', 'CCK', 'COL', 'COM', 'COD', 'COG', 'COK', 'CRI', 'CIV', 'HRV',
                   'CUB', 'CUW', 'CYP', 'CZE', 'DNK', 'DJI', 'DMA', 'DOM', 'ECU', 'EGY', 'SLV', 'GNQ', 'ERI', 'EST',
                   'SWZ', 'ETH', 'FLK', 'FRO', 'FJI', 'FIN', 'FRA', 'GUF', 'PYF', 'ATF', 'GAB', 'GMB', 'GEO', 'DEU',
                   'GHA', 'GIB', 'GRC', 'GRL', 'GRD', 'GLP', 'GUM', 'GTM', 'GGY', 'GIN', 'GNB', 'GUY', 'HTI', 'HMD',
                   'VAT', 'HND', 'HKG', 'HUN', 'ISL', 'IND', 'IDN', 'IRN', 'IRQ', 'IRL', 'IMN', 'ISR', 'ITA', 'JAM',
                   'JPN', 'JEY', 'JOR', 'KAZ', 'KEN', 'KIR', 'PRK', 'KOR', 'KWT', 'KGZ', 'LAO',
                   'LVA', 'LBN', 'LSO', 'LBR', 'LBY', 'LIE', 'LTU', 'LUX', 'MAC', 'MKD', 'MDG', 'MWI', 'MYS', 'MDV',
                   'MLI', 'MLT', 'MHL', 'MTQ', 'MRT', 'MUS', 'MYT', 'MEX', 'FSM', 'MDA', 'MCO', 'MNG', 'MNE', 'MSR',
                   'MAR', 'MOZ', 'MMR', 'NAM', 'NRU', 'NPL', 'NLD', 'NCL', 'NZL', 'NIC', 'NER', 'NGA', 'NIU', 'NFK',
                   'MNP', 'NOR', 'OMN', 'PAK', 'PLW', 'PSE', 'PAN', 'PNG', 'PRY', 'PER', 'PHL', 'PCN', 'POL', 'PRT',
                   'PRI', 'QAT', 'REU', 'ROU', 'RUS', 'RWA', 'BLM', 'SHN', 'KNA', 'LCA', 'MAF', 'SPM', 'VCT', 'WSM',
                   'SMR', 'STP', 'SAU', 'SEN', 'SRB', 'SYC', 'SLE', 'SGP', 'SXM', 'SVK', 'SVN', 'SLB', 'SOM', 'ZAF',
                   'SGS', 'SSD', 'ESP', 'LKA', 'SDN', 'SUR', 'SJM', 'SWE', 'CHE', 'SYR', 'TWN', 'TJK', 'TZA', 'THA',
                   'TLS', 'TGO', 'TKL', 'TON', 'TTO', 'TUN', 'TUR', 'TKM', 'TCA', 'TUV', 'UGA', 'UKR', 'ARE', 'GBR',
                   'UMI', 'USA', 'URY', 'UZB', 'VUT', 'VEN', 'VNM', 'VGB', 'VIR', 'WLF', 'ESH', 'YEM', 'ZMB', 'ZWE']

flyway_fileName = 'V1_103__insert_into_country_temperature_table.sql'
path_dir = './src/flyway/sql/'


def convertNaNtoNull(res):
    for key in res.keys():
        if res.get(key) == 'NaN':
            res[key] = 'null'
    return res


def sendRequestAndMakeFile():
    newFile = open(path_dir + flyway_fileName, 'w', encoding='UTF-8')

    no_data_country = []

    startLine = "INSERT INTO country_temperature VALUES \n"
    for i in range(len(ALPHA3CODE_LIST)):
        res = convertNaNtoNull(requests.get(
            BASE_URL + ALPHA3CODE_LIST[i]).json())
        row = ""
        if len(res) == 0:
            no_data_country.append(ALPHA3CODE_LIST[i])
            continue
        if i % 50 == 0:
            row += startLine
        row += "( '" + ALPHA3CODE_LIST[i] + "', " + res.get("year_1901") + ", " + res.get("year_1902") + ", " + res.get(
            "year_1903") + ", " + res.get("year_1904") + ", " + res.get("year_1905") + ", " + res.get("year_1906") + ", " + res.get(
            "year_1907") + ", " + res.get("year_1908") + ", " + res.get("year_1909") + ", " + res.get("year_1910") + ", " + res.get(
            "year_1911") + ", " + res.get("year_1912") + ", " + res.get("year_1913") + ", " + res.get("year_1914") + ", " + res.get(
            "year_1915") + ", " + res.get("year_1916") + ", " + res.get("year_1917") + ", " + res.get("year_1918") + ", " + res.get(
            "year_1919") + ", " + res.get("year_1920") + ", " + res.get("year_1921") + ", " + res.get("year_1922") + ", " + res.get(
            "year_1923") + ", " + res.get("year_1924") + ", " + res.get("year_1925") + ", " + res.get("year_1926") + ", " + res.get(
            "year_1927") + ", " + res.get("year_1928") + ", " + res.get("year_1929") + ", " + res.get("year_1930") + ", " + res.get(
            "year_1931") + ", " + res.get("year_1932") + ", " + res.get("year_1933") + ", " + res.get("year_1934") + ", " + res.get(
            "year_1935") + ", " + res.get("year_1936") + ", " + res.get("year_1937") + ", " + res.get("year_1938") + ", " + res.get(
            "year_1939") + ", " + res.get("year_1940") + ", " + res.get("year_1941") + ", " + res.get("year_1942") + ", " + res.get(
            "year_1943") + ", " + res.get("year_1944") + ", " + res.get("year_1945") + ", " + res.get("year_1946") + ", " + res.get(
            "year_1947") + ", " + res.get("year_1948") + ", " + res.get("year_1949") + ", " + res.get("year_1950") + ", " + res.get(
            "year_1951") + ", " + res.get("year_1952") + ", " + res.get("year_1953") + ", " + res.get("year_1954") + ", " + res.get(
            "year_1955") + ", " + res.get("year_1956") + ", " + res.get("year_1957") + ", " + res.get("year_1958") + ", " + res.get(
            "year_1959") + ", " + res.get("year_1960") + ", " + res.get("year_1961") + ", " + res.get("year_1962") + ", " + res.get(
            "year_1963") + ", " + res.get("year_1964") + ", " + res.get("year_1965") + ", " + res.get("year_1966") + ", " + res.get(
            "year_1967") + ", " + res.get("year_1968") + ", " + res.get("year_1969") + ", " + res.get("year_1970") + ", " + res.get(
            "year_1971") + ", " + res.get("year_1972") + ", " + res.get("year_1973") + ", " + res.get("year_1974") + ", " + res.get(
            "year_1975") + ", " + res.get("year_1976") + ", " + res.get("year_1977") + ", " + res.get("year_1978") + ", " + res.get(
            "year_1979") + ", " + res.get("year_1980") + ", " + res.get("year_1981") + ", " + res.get("year_1982") + ", " + res.get(
            "year_1983") + ", " + res.get("year_1984") + ", " + res.get("year_1985") + ", " + res.get("year_1986") + ", " + res.get(
            "year_1987") + ", " + res.get("year_1988") + ", " + res.get("year_1989") + ", " + res.get("year_1990") + ", " + res.get(
            "year_1991") + ", " + res.get("year_1992") + ", " + res.get("year_1993") + ", " + res.get("year_1994") + ", " + res.get(
            "year_1995") + ", " + res.get("year_1996") + ", " + res.get("year_1997") + ", " + res.get("year_1998") + ", " + res.get(
            "year_1999") + ", " + res.get("year_2000") + ", " + res.get("year_2001") + ", " + res.get("year_2002") + ", " + res.get(
            "year_2003") + ", " + res.get("year_2004") + ", " + res.get("year_2005") + ", " + res.get("year_2006") + ", " + res.get(
            "year_2007") + ", " + res.get("year_2008") + ", " + res.get("year_2009") + ", " + res.get("year_2010") + ", " + res.get(
            "year_2011") + ", " + res.get("year_2012") + ", " + res.get("year_2013") + ", " + res.get("year_2014") + ", " + res.get(
            "year_2015") + ", " + res.get("year_2016") + ", " + res.get("year_2017") + ", " + res.get("year_2018") + ", " + res.get(
            "year_2019") + ", " + res.get("year_2020") + ")"

        if (i + 1) % 50 == 0 or i == len(ALPHA3CODE_LIST) - 1:
            row += "; \n"
        elif (i + 1) % 50 != 0:
            row += ", \n"
        newFile.write(row)

    for ele in no_data_country:
        row = "INSERT INTO country_temperature (alpha3_code) VALUES ('" + \
            ele + "');"
        newFile.write(row)


if __name__ == '__main__':
    if not Common.checkIfFileExists(flyway_fileName):
        sendRequestAndMakeFile()
