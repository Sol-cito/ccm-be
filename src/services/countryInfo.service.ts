import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { CountryCode } from 'src/entities/countryCode.entity';
import { CountryInfoRawQueryRepository } from 'src/rawQuery/countryInfoRawQuery.repository';
import { CountryCodeRepository } from 'src/repositories/countryCode.repository';
import { Repository } from 'typeorm';

@Injectable()
export class CountryInfoService {
  constructor(
    @InjectRepository(CountryCodeRepository)
    private readonly countryCodeRepository: Repository<CountryCode>,
    private readonly countryInfoRawQueryRepository: CountryInfoRawQueryRepository,
  ) {}

  async getAllCountryCode(): Promise<CountryCode[]> {
    return await this.countryCodeRepository.find();
  }

  async getCountryTemperature(countryCode: string): Promise<any> {
    const countryCodeRes: CountryCode =
      await this.countryCodeRepository.findOne({
        where: { alpha2Code: countryCode },
      });
    const tempRes = this.countryInfoRawQueryRepository.getCountryTemperature(
      countryCodeRes.alpha3Code,
    );
    return tempRes;
  }
}
