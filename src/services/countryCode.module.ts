import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { CountryCodeRepository } from 'src/repositories/countryCode.repository';
import { CountryCodeController } from './countryCode.controller';
import { CountryCodeService } from './countryCode.service';

@Module({
  imports: [TypeOrmModule.forFeature([CountryCodeRepository])],
  controllers: [CountryCodeController],
  providers: [CountryCodeService],
})
export class CountryCodeModule {}
