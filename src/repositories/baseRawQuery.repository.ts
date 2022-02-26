import { createConnection } from 'typeorm';

export class BaseRawQueryRepository {
  protected async executeQuery(rawQuery: string): Promise<any> {
    let connection;
    try {
      connection = await createConnection({
        name: 'temp',
        type: 'mysql',
        host: 'localhost',
        port: 3307,
        username: 'root',
        password: 'myPassword123',
        database: 'ccm',
      });
      const result = await connection.query(rawQuery);
      await connection.commit();
      return result;
    } catch (error) {
      if (connection) {
        await connection.rollback();
      }
      // TO-DO 공통 에러처리
      console.log(error);
    } finally {
      if (connection) {
        await connection.close();
      }
    }
  }
}
