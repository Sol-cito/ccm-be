import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World yeah!';
  }

  getTest(): string {
    return 'Hey bitch'
  }
}
