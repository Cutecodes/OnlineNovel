USE NovelWebsite
GO
IF OBJECT_ID('CHAPTER','U') IS NOT NULL
   DROP TABLE CHAPTER
GO
CREATE TABLE CHAPTER
(
NovelID INT NOT NULL IDENTITY(1,1),
ChapterNum VARCHAR(5) NOT NULL,
UpdateTime DATE NULL,
ChapterState NVARCHAR(5) NOT NULL,--RANGE
CONSTRAINT ChapterPK PRIMARY KEY(NovelID,ChapterNum),
CONSTRAINT NovelFK1 FOREIGN KEY(NovelID)
           REFERENCES NOVEl(NovelID)
		           ON UPDATE NO ACTION 
				   ON DELETE NO ACTION,
CONSTRAINT ValidChapterNum CHECK 
           (ChapterNum IN ('�����','����','������'))
);
GO
--TEST
--SELECT * FROM CHAPTER
