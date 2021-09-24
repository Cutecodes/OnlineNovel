USE NovelWebsite
GO
IF OBJECT_ID('EditorView','V') IS NOT NULL--V ”Õº
  DROP VIEW EditorView
GO
CREATE VIEW EditorView WITH SCHEMABINDING
AS
SELECT E.EditorID,E.Salary,A.AuthorID,N.NovelName,CP.ChapterNum,CP.ChapterState
FROM dbo.EDITOR E INNER JOIN dbo.IN_CHARGE_OF ICF ON E.EditorID=ICF.EditorID
INNER JOIN dbo.AUTHOR A ON A.AuthorID=ICF.AuthorID
INNER JOIN dbo.Novel N  ON A.AuthorID=N.AuthorID 
INNER JOIN dbo.CHAPTER CP ON CP.NovelID=N.NovelID
GO
--TEST
--SELECT * FROM EditorView