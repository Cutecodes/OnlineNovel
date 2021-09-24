USE NovelWebsite
GO
IF OBJECT_ID('tigger_InsertSubscribe','TR') IS NOT NULL
  DROP TRIGGER tigger_InsertSubscribe
GO 
CREATE TRIGGER tigger_InsertSubscribe
ON SUBSCRIBE AFTER INSERT
AS
UPDATE READER SET Points=Points-(SELECT Price FROM SUBSCRIBE)
                          *(SELECT COUNT(ChapterNum)
                            FROM inserted
						    GROUP BY ReaderID
							HAVING READER.ReaderID=inserted.ReaderID)
WHERE READER.Points>(SELECT Price FROM SUBSCRIBE)
                          *(SELECT COUNT(ChapterNum)
                            FROM inserted
						    GROUP BY ReaderID
							HAVING READER.ReaderID=inserted.ReaderID)
GO
