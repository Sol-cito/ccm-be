import { Controller, Get, Logger, Query } from '@nestjs/common';
import { CountryCode } from 'src/entities/countryCode.entity';
import { CountryInfoService } from './countryInfo.service';

@Controller('countryInfo')
export class CountryInfoController {
  private readonly logger = new Logger(CountryInfoController.name);
  constructor(private readonly countryInfoService: CountryInfoService) {}

  @Get('allCode')
  getAllCountryCode(): Promise<CountryCode[]> {
    this.logger.log('Execute getAllCountryCode()');
    return this.countryInfoService.getAllCountryCode();
  }

  @Get('temperature')
  getCountryTemperature(@Query('countryCode') countryCode): Promise<any> {
    this.logger.log('Execute getCountryTemperature()');
    return this.countryInfoService.getCountryTemperature(countryCode);
  }
}
