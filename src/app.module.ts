import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Connection } from 'typeorm';
import { CountryCodeModule } from './services/countryCode.module';

@Module({
  imports: [TypeOrmModule.forRoot(), CountryCodeModule],
  controllers: [],
  providers: [],
})
export class AppModule {
  constructor(private readonly connection: Connection) {}
}
