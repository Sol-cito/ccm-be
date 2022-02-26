import { Controller, Get, Query } from '@nestjs/common';
import { CountryCode } from 'src/entities/countryCode.entity';
// import { CountryTemperature } from 'src/entities/countryTemperature.entity';
import { CountryInfoService } from './countryInfo.service';

@Controller('countryInfo')
export class CountryInfoController {
  constructor(private readonly countryInfoService: CountryInfoService) {}

  @Get('allCode')
  getAllCountryCode(): Promise<CountryCode[]> {
    return this.countryInfoService.getAllCountryCode();
  }

  @Get('temperature')
  getCountryTemperature(@Query('countryCode') countryCode): Promise<any> {
    return this.countryInfoService.getCountryTemperature(countryCode);
  }
}
