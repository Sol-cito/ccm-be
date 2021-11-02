import { Controller, Get } from '@nestjs/common';
import { CountryCode } from 'src/entities/countryCode.entity';
import { CountryCodeService } from './countryCode.service';

@Controller('countryCode')
export class CountryCodeController {
  constructor(private readonly countryCodeService: CountryCodeService) {}

  @Get('test')
  getHello(): string {
    return this.countryCodeService.getTest();
  }

  @Get('allCode')
  getAllCountryCode(): Promise<CountryCode[]> {
    return this.countryCodeService.getAllCountryCode();
  }
}
