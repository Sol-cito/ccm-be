import { CountryCode } from 'src/entities/countryCode.entity';
import { EntityRepository, Repository } from 'typeorm';

@EntityRepository(CountryCode)
export class CountryCodeRepository extends Repository<CountryCode> {}
