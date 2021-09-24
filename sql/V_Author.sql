USE NovelWebsite
GO
IF OBJECT_ID('AuthorView','V') IS NOT NULL--V ”Õº
  DROP VIEW AuthorView
GO
CREATE VIEW AuthorView WITH SCHEMABINDING
AS
SELECT A.AuthorID,A.Points,N.NovelName,N.NovelType,N.NovelState,N.Cover,N.NovelProfile,CP.ChapterNum,CP.UpdateTime,CP.ChapterState
FROM dbo.AUTHOR A INNER JOIN dbo.Novel N ON A.AuthorID=N.AuthorID
INNER JOIN dbo.CHAPTER CP ON N.NovelID=CP.NovelID
GO
--TEST
--SELECT * FROM AuthorView