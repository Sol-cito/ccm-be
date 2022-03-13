import { Injectable, Logger } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { CountryCode } from 'src/entities/countryCode.entity';
import { CountryInfoRawQueryRepository } from 'src/rawQuery/countryInfoRawQuery.repository';
import { CountryCodeRepository } from 'src/repositories/countryCode.repository';
import { Repository } from 'typeorm';

@Injectable()
export class CountryInfoService {
  private readonly logger = new Logger(CountryInfoService.name);

  constructor(
    @InjectRepository(CountryCodeRepository)
    private readonly countryCodeRepository: Repository<CountryCode>,
    private readonly countryInfoRawQueryRepository: CountryInfoRawQueryRepository,
  ) {}

  async getAllCountryCode(): Promise<CountryCode[]> {
    this.logger.log('Execute getAllCountryCode()');
    return await this.countryCodeRepository.find();
  }

  async getCountryTemperature(countryCode: string): Promise<any> {
    this.logger.log('Execute getCountryTemperature()');
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
