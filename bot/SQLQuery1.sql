-- បង្កើត Database (បើមិនទាន់មាន)
CREATE DATABASE TelegramBotDB;
GO

USE TelegramBotDB;
GO

-- បង្កើត Table សម្រាប់កត់ត្រាសារ
CREATE TABLE ChatLogs (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    UserId BIGINT,
    UserName NVARCHAR(100),
    CustomerMessage NVARCHAR(MAX),
    BotReply NVARCHAR(MAX),
    CreatedAt DATETIME DEFAULT GETDATE()
);
GO
