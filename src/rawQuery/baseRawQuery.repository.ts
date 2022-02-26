import { getConnection } from 'typeorm';

export class BaseRawQueryRepository {
  protected async executeQuery(rawQuery: string): Promise<any> {
    const conn = getConnection();
    const queryRunner = conn.createQueryRunner();
    await queryRunner.connect();
    await queryRunner.startTransaction();
    let result;
    try {
      result = await queryRunner.query(rawQuery);
      await queryRunner.commitTransaction();
      return result;
    } catch (error) {
      if (queryRunner) {
        await queryRunner.rollbackTransaction();
      }
      // TO-DO 공통 에러처리
      console.log(error);
    } finally {
      if (queryRunner) {
        await queryRunner.release();
      }
    }
  }
}
