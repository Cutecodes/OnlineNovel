USE NovelWebsite
GO
IF OBJECT_ID('NOVEL','U') IS NOT NULL--U�û��Զ����
  DROP TABLE NOVEL
GO
CREATE TABLE NOVEL
(
NovelID INT NOT NULL IDENTITY(1,1),--SK,PK
NovelName NVARCHAR(15) NOT NULL,--Unicode
AuthorID char(10) NOT NULL,--FK1
NovelType NVARCHAR(5) NOT NULL,--range
Cover IMAGE NULL,
NovelState NVARCHAR(5) NOT NULL,--range
NovelProfile text NULL,
CONSTRAINT NovelPK PRIMARY KEY(NovelID),
CONSTRAINT AuthorFK FOREIGN KEY(AuthorID)
           REFERENCES AUTHOR(AuthorID)
		           ON UPDATE NO ACTION
				   ON DELETE NO ACTION,
CONSTRAINT ValidType CHECK
           (NovelType IN ('����','����','�촩','����','����','����')),
CONSTRAINT ValidState CHECK
           (NovelState IN ('����','���'))
);
GO
--TEST
--SELECT * FROM NOVEL

