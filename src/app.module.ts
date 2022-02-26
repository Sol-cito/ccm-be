import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Connection } from 'typeorm';
import { CountryInfoModule } from './services/countryInfo.module';

@Module({
  imports: [TypeOrmModule.forRoot(), CountryInfoModule],
  controllers: [],
  providers: [],
})
export class AppModule {
  constructor(private readonly connection: Connection) {}
}
