USE NovelWebsite
GO
IF OBJECT_ID('NovelView','V') IS NOT NULL--V ”Õº
  DROP VIEW NovelView
GO
CREATE VIEW NovelView WITH SCHEMABINDING
AS
SELECT NovelName,AuthorID,NovelType,Cover,NovelState,NovelProfile,ChapterNum
FROM dbo.NOVEL INNER JOIN dbo.CHAPTER ON NOVEL.NovelID=CHAPTER.NovelID
GO
--TEST
--SELECT * FROM NovelView
