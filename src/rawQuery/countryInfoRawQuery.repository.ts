import { TemperatureByAlpha3Code } from 'src/rawQuery/countryInfo.query';
import { BaseRawQueryRepository } from './baseRawQuery.repository';

export class CountryInfoRawQueryRepository extends BaseRawQueryRepository {
  async getCountryTemperature(alpha3Code: string) {
    const query = TemperatureByAlpha3Code(alpha3Code);
    const res = this.executeQuery(query);
    return res;
  }
}
