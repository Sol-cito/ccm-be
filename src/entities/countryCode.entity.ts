import { BaseEntity, Column, Entity, PrimaryGeneratedColumn } from 'typeorm';

@Entity('country_code')
export class CountryCode extends BaseEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ name: 'country_name', type: 'varchar' })
  countryName: string;

  @Column({ name: 'alpha2_code' })
  alpha2Code: string;

  @Column({ name: 'alpha3_code' })
  alpha3Code: string;

  @Column({ name: 'numeric_code' })
  numericCode: number;
}
