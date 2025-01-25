       IDENTIFICATION DIVISION.
       PROGRAM-ID. AddNumbersFunction.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  NUM1              PIC 9(5) VALUE 12345.
       01  NUM2              PIC 9(5) VALUE 54321.
       01  RESULT            PIC 9(5) VALUE 0.

       LINKAGE SECTION.
       01  PARAM1            PIC 9(5).
       01  PARAM2            PIC 9(5).
       01  FUNCTION-RESULT   PIC 9(5).

       PROCEDURE DIVISION.
       MAIN-PARA.
           CALL 'ADD-FUNCTION' USING NUM1 NUM2 RESULT.

           DISPLAY "The result of addition is: " RESULT.

           STOP RUN.

       ADD-FUNCTION SECTION.
       ADD-PARA.
           ADD PARAM1 TO PARAM2 GIVING FUNCTION-RESULT.
           EXIT SECTION.
