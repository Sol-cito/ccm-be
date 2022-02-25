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
        row += "( '" + ALPHA3CODE_LIST[i] + "', " + res.get("1901") + ", " + res.get("1902") + ", " + res.get(
            "1903") + ", " + res.get("1904") + ", " + res.get("1905") + ", " + res.get("1906") + ", " + res.get(
            "1907") + ", " + res.get("1908") + ", " + res.get("1909") + ", " + res.get("1910") + ", " + res.get(
            "1911") + ", " + res.get("1912") + ", " + res.get("1913") + ", " + res.get("1914") + ", " + res.get(
            "1915") + ", " + res.get("1916") + ", " + res.get("1917") + ", " + res.get("1918") + ", " + res.get(
            "1919") + ", " + res.get("1920") + ", " + res.get("1921") + ", " + res.get("1922") + ", " + res.get(
            "1923") + ", " + res.get("1924") + ", " + res.get("1925") + ", " + res.get("1926") + ", " + res.get(
            "1927") + ", " + res.get("1928") + ", " + res.get("1929") + ", " + res.get("1930") + ", " + res.get(
            "1931") + ", " + res.get("1932") + ", " + res.get("1933") + ", " + res.get("1934") + ", " + res.get(
            "1935") + ", " + res.get("1936") + ", " + res.get("1937") + ", " + res.get("1938") + ", " + res.get(
            "1939") + ", " + res.get("1940") + ", " + res.get("1941") + ", " + res.get("1942") + ", " + res.get(
            "1943") + ", " + res.get("1944") + ", " + res.get("1945") + ", " + res.get("1946") + ", " + res.get(
            "1947") + ", " + res.get("1948") + ", " + res.get("1949") + ", " + res.get("1950") + ", " + res.get(
            "1951") + ", " + res.get("1952") + ", " + res.get("1953") + ", " + res.get("1954") + ", " + res.get(
            "1955") + ", " + res.get("1956") + ", " + res.get("1957") + ", " + res.get("1958") + ", " + res.get(
            "1959") + ", " + res.get("1960") + ", " + res.get("1961") + ", " + res.get("1962") + ", " + res.get(
            "1963") + ", " + res.get("1964") + ", " + res.get("1965") + ", " + res.get("1966") + ", " + res.get(
            "1967") + ", " + res.get("1968") + ", " + res.get("1969") + ", " + res.get("1970") + ", " + res.get(
            "1971") + ", " + res.get("1972") + ", " + res.get("1973") + ", " + res.get("1974") + ", " + res.get(
            "1975") + ", " + res.get("1976") + ", " + res.get("1977") + ", " + res.get("1978") + ", " + res.get(
            "1979") + ", " + res.get("1980") + ", " + res.get("1981") + ", " + res.get("1982") + ", " + res.get(
            "1983") + ", " + res.get("1984") + ", " + res.get("1985") + ", " + res.get("1986") + ", " + res.get(
            "1987") + ", " + res.get("1988") + ", " + res.get("1989") + ", " + res.get("1990") + ", " + res.get(
            "1991") + ", " + res.get("1992") + ", " + res.get("1993") + ", " + res.get("1994") + ", " + res.get(
            "1995") + ", " + res.get("1996") + ", " + res.get("1997") + ", " + res.get("1998") + ", " + res.get(
            "1999") + ", " + res.get("2000") + ", " + res.get("2001") + ", " + res.get("2002") + ", " + res.get(
            "2003") + ", " + res.get("2004") + ", " + res.get("2005") + ", " + res.get("2006") + ", " + res.get(
            "2007") + ", " + res.get("2008") + ", " + res.get("2009") + ", " + res.get("2010") + ", " + res.get(
            "2011") + ", " + res.get("2012") + ", " + res.get("2013") + ", " + res.get("2014") + ", " + res.get(
            "2015") + ", " + res.get("2016") + ", " + res.get("2017") + ", " + res.get("2018") + ", " + res.get(
            "2019") + ", " + res.get("2020") + ")"

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
