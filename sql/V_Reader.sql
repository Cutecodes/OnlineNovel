USE NovelWebsite
GO
IF OBJECT_ID('ReaderView','V') IS NOT NULL--V??ͼ
  DROP VIEW ReaderView
GO
CREATE VIEW ReaderView WITH SCHEMABINDING
AS
SELECT R.ReaderID,Points,C.NovelID,ChapterNum
FROM dbo.READER R INNER JOIN dbo.COLLECTIONS C ON R.ReaderID=C.ReaderID
INNER JOIN dbo.CHAPTER CP ON C.NovelID=CP.NovelID
GROUP BY R.ReaderID,C.NovelID,CP.ChapterNum,Points
GO
--TEST
--SELECT * FROM ReaderView