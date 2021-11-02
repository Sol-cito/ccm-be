import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { CountryCode } from 'src/entities/countryCode.entity';
import { CountryCodeRepository } from 'src/repositories/countryCode.repository';
import { Repository } from 'typeorm';

@Injectable()
export class CountryCodeService {
  constructor(
    @InjectRepository(CountryCodeRepository)
    private readonly countryCodeRepository: Repository<CountryCode>,
  ) {}

  getAllCountryCode(): Promise<CountryCode[]> {
    return this.countryCodeRepository.find();
  }

  getTest(): string {
    return 'Hey test';
  }
}
