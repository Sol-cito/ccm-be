import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { CountryInfoRawQueryRepository } from 'src/rawQuery/countryInfoRawQuery.repository';
import { CountryCodeRepository } from 'src/repositories/countryCode.repository';
import { CountryInfoController } from './countryInfo.controller';
import { CountryInfoService } from './countryInfo.service';

@Module({
  imports: [TypeOrmModule.forFeature([CountryCodeRepository])],
  controllers: [CountryInfoController],
  providers: [CountryInfoService, CountryInfoRawQueryRepository],
})
export class CountryInfoModule {}
