from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `student` DROP INDEX `email`;
        ALTER TABLE `student` DROP COLUMN `email`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `student` ADD `email` VARCHAR(100) NOT NULL UNIQUE COMMENT '邮件';
        ALTER TABLE `student` ADD UNIQUE INDEX `email` (`email`);"""
