; ModuleID = 'uat_test3_annotated.bc'
source_filename = "uat_test3_annotated.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str = private unnamed_addr constant [42 x i8] c"\0A\0A\09\09Studytonight - Best place to learn\0A\0A\0A\00", align 1
@.str.1 = private unnamed_addr constant [22 x i8] c"\0A\0AEnter a string :   \00", align 1
@.str.2 = private unnamed_addr constant [41 x i8] c"\0A\0ANumber of vowels in string '%s' is: %d\00", align 1
@.str.3 = private unnamed_addr constant [26 x i8] c"\0A\0A\0A\0A\09\09\09Coding is Fun !\0A\0A\0A\00", align 1
@.str.4 = private unnamed_addr constant [5 x i8] c"flag\00", align 1

; Function Attrs: noinline nounwind uwtable
define i32 @main() #0 !dbg !7 {
entry:
  %retval = alloca i32, align 4
  %aj = alloca [100 x i8], align 16
  %mj = alloca i32, align 4
  store i32 0, i32* %retval, align 4
  %call = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([42 x i8], [42 x i8]* @.str, i32 0, i32 0)), !dbg !11
  call void @llvm.dbg.declare(metadata [100 x i8]* %aj, metadata !12, metadata !DIExpression()), !dbg !17
  call void @llvm.dbg.declare(metadata i32* %mj, metadata !18, metadata !DIExpression()), !dbg !19
  %call1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([22 x i8], [22 x i8]* @.str.1, i32 0, i32 0)), !dbg !20
  %arraydecay = getelementptr inbounds [100 x i8], [100 x i8]* %aj, i32 0, i32 0, !dbg !21
  %call2 = call i32 (i8*, ...) bitcast (i32 (...)* @gets to i32 (i8*, ...)*)(i8* %arraydecay), !dbg !22
  %arraydecay3 = getelementptr inbounds [100 x i8], [100 x i8]* %aj, i32 0, i32 0, !dbg !23
  %call4 = call i32 @count_vowels(i8* %arraydecay3), !dbg !24
  store i32 %call4, i32* %mj, align 4, !dbg !25
  %arraydecay5 = getelementptr inbounds [100 x i8], [100 x i8]* %aj, i32 0, i32 0, !dbg !26
  %0 = load i32, i32* %mj, align 4, !dbg !27
  %call6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i8* %arraydecay5, i32 %0), !dbg !28
  %call7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([26 x i8], [26 x i8]* @.str.3, i32 0, i32 0)), !dbg !29
  ret i32 0, !dbg !30
}

declare i32 @printf(i8*, ...) #1

; Function Attrs: nounwind readnone speculatable
declare void @llvm.dbg.declare(metadata, metadata, metadata) #2

declare i32 @gets(...) #1

; Function Attrs: noinline nounwind uwtable
define i32 @count_vowels(i8* %adi) #0 !dbg !31 {
entry:
  %adi.addr = alloca i8*, align 8
  %count = alloca i32, align 4
  %c = alloca i32, align 4
  %flag = alloca i32, align 4
  %d = alloca i8, align 1
  store i8* %adi, i8** %adi.addr, align 8
  call void @llvm.dbg.declare(metadata i8** %adi.addr, metadata !35, metadata !DIExpression()), !dbg !36
  call void @llvm.dbg.declare(metadata i32* %count, metadata !37, metadata !DIExpression()), !dbg !38
  store i32 0, i32* %count, align 4, !dbg !38
  call void @llvm.dbg.declare(metadata i32* %c, metadata !39, metadata !DIExpression()), !dbg !40
  store i32 0, i32* %c, align 4, !dbg !40
  call void @llvm.dbg.declare(metadata i32* %flag, metadata !41, metadata !DIExpression()), !dbg !42
  store i32 0, i32* %flag, align 4, !dbg !42
  %0 = bitcast i32* %flag to i8*, !dbg !43
  call void @klee_make_symbolic(i8* %0, i64 4, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.4, i32 0, i32 0)), !dbg !44
  call void @llvm.dbg.declare(metadata i8* %d, metadata !45, metadata !DIExpression()), !dbg !46
  br label %do.body, !dbg !47, !llvm.loop !48

do.body:                                          ; preds = %if.end, %entry
  %1 = load i8*, i8** %adi.addr, align 8, !dbg !50
  %2 = load i32, i32* %c, align 4, !dbg !52
  %idxprom = sext i32 %2 to i64, !dbg !50
  %arrayidx = getelementptr inbounds i8, i8* %1, i64 %idxprom, !dbg !50
  %3 = load i8, i8* %arrayidx, align 1, !dbg !50
  store i8 %3, i8* %d, align 1, !dbg !53
  %4 = load i8, i8* %d, align 1, !dbg !54
  %call = call i32 @check_vowel(i8 signext %4), !dbg !55
  store i32 %call, i32* %flag, align 4, !dbg !56
  %5 = load i32, i32* %flag, align 4, !dbg !57
  %cmp = icmp eq i32 %5, 1, !dbg !59
  br i1 %cmp, label %if.then, label %if.end, !dbg !60

if.then:                                          ; preds = %do.body
  %6 = load i32, i32* %count, align 4, !dbg !61
  %inc = add nsw i32 %6, 1, !dbg !61
  store i32 %inc, i32* %count, align 4, !dbg !61
  br label %if.end, !dbg !63

if.end:                                           ; preds = %if.then, %do.body
  %7 = load i32, i32* %c, align 4, !dbg !64
  %inc1 = add nsw i32 %7, 1, !dbg !64
  store i32 %inc1, i32* %c, align 4, !dbg !64
  %8 = load i8, i8* %d, align 1, !dbg !65
  %conv = sext i8 %8 to i32, !dbg !65
  %cmp2 = icmp ne i32 %conv, 0, !dbg !66
  br i1 %cmp2, label %do.body, label %do.end, !dbg !67, !llvm.loop !48

do.end:                                           ; preds = %if.end
  %9 = load i32, i32* %count, align 4, !dbg !68
  ret i32 %9, !dbg !69
}

declare void @klee_make_symbolic(i8*, i64, i8*) #1

; Function Attrs: noinline nounwind uwtable
define i32 @check_vowel(i8 signext %ajj) #0 !dbg !70 {
entry:
  %retval = alloca i32, align 4
  %ajj.addr = alloca i8, align 1
  store i8 %ajj, i8* %ajj.addr, align 1
  call void @llvm.dbg.declare(metadata i8* %ajj.addr, metadata !73, metadata !DIExpression()), !dbg !74
  %0 = load i8, i8* %ajj.addr, align 1, !dbg !75
  %conv = sext i8 %0 to i32, !dbg !75
  %cmp = icmp sge i32 %conv, 65, !dbg !77
  br i1 %cmp, label %land.lhs.true, label %if.end, !dbg !78

land.lhs.true:                                    ; preds = %entry
  %1 = load i8, i8* %ajj.addr, align 1, !dbg !79
  %conv2 = sext i8 %1 to i32, !dbg !79
  %cmp3 = icmp sle i32 %conv2, 90, !dbg !80
  br i1 %cmp3, label %if.then, label %if.end, !dbg !81

if.then:                                          ; preds = %land.lhs.true
  %2 = load i8, i8* %ajj.addr, align 1, !dbg !82
  %conv5 = sext i8 %2 to i32, !dbg !82
  %add = add nsw i32 %conv5, 97, !dbg !83
  %sub = sub nsw i32 %add, 65, !dbg !84
  %conv6 = trunc i32 %sub to i8, !dbg !82
  store i8 %conv6, i8* %ajj.addr, align 1, !dbg !85
  br label %if.end, !dbg !86

if.end:                                           ; preds = %if.then, %land.lhs.true, %entry
  %3 = load i8, i8* %ajj.addr, align 1, !dbg !87
  %conv7 = sext i8 %3 to i32, !dbg !87
  %cmp8 = icmp eq i32 %conv7, 97, !dbg !89
  br i1 %cmp8, label %if.then25, label %lor.lhs.false, !dbg !90

lor.lhs.false:                                    ; preds = %if.end
  %4 = load i8, i8* %ajj.addr, align 1, !dbg !91
  %conv10 = sext i8 %4 to i32, !dbg !91
  %cmp11 = icmp eq i32 %conv10, 101, !dbg !92
  br i1 %cmp11, label %if.then25, label %lor.lhs.false13, !dbg !93

lor.lhs.false13:                                  ; preds = %lor.lhs.false
  %5 = load i8, i8* %ajj.addr, align 1, !dbg !94
  %conv14 = sext i8 %5 to i32, !dbg !94
  %cmp15 = icmp eq i32 %conv14, 105, !dbg !95
  br i1 %cmp15, label %if.then25, label %lor.lhs.false17, !dbg !96

lor.lhs.false17:                                  ; preds = %lor.lhs.false13
  %6 = load i8, i8* %ajj.addr, align 1, !dbg !97
  %conv18 = sext i8 %6 to i32, !dbg !97
  %cmp19 = icmp eq i32 %conv18, 111, !dbg !98
  br i1 %cmp19, label %if.then25, label %lor.lhs.false21, !dbg !99

lor.lhs.false21:                                  ; preds = %lor.lhs.false17
  %7 = load i8, i8* %ajj.addr, align 1, !dbg !100
  %conv22 = sext i8 %7 to i32, !dbg !100
  %cmp23 = icmp eq i32 %conv22, 117, !dbg !101
  br i1 %cmp23, label %if.then25, label %if.end26, !dbg !102

if.then25:                                        ; preds = %lor.lhs.false21, %lor.lhs.false17, %lor.lhs.false13, %lor.lhs.false, %if.end
  store i32 1, i32* %retval, align 4, !dbg !103
  br label %return, !dbg !103

if.end26:                                         ; preds = %lor.lhs.false21
  store i32 0, i32* %retval, align 4, !dbg !104
  br label %return, !dbg !104

return:                                           ; preds = %if.end26, %if.then25
  %8 = load i32, i32* %retval, align 4, !dbg !105
  ret i32 %8, !dbg !105
}

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind readnone speculatable }

!llvm.dbg.cu = !{!0}
!llvm.module.flags = !{!3, !4, !5}
!llvm.ident = !{!6}

!0 = distinct !DICompileUnit(language: DW_LANG_C99, file: !1, producer: "clang version 6.0.1 ", isOptimized: false, runtimeVersion: 0, emissionKind: FullDebug, enums: !2)
!1 = !DIFile(filename: "uat_test3_annotated.c", directory: "/home/klee/FYP/clean_UAT/UAT")
!2 = !{}
!3 = !{i32 2, !"Dwarf Version", i32 4}
!4 = !{i32 2, !"Debug Info Version", i32 3}
!5 = !{i32 1, !"wchar_size", i32 4}
!6 = !{!"clang version 6.0.1 "}
!7 = distinct !DISubprogram(name: "main", scope: !1, file: !1, line: 8, type: !8, isLocal: false, isDefinition: true, scopeLine: 9, isOptimized: false, unit: !0, variables: !2)
!8 = !DISubroutineType(types: !9)
!9 = !{!10}
!10 = !DIBasicType(name: "int", size: 32, encoding: DW_ATE_signed)
!11 = !DILocation(line: 10, column: 5, scope: !7)
!12 = !DILocalVariable(name: "aj", scope: !7, file: !1, line: 11, type: !13)
!13 = !DICompositeType(tag: DW_TAG_array_type, baseType: !14, size: 800, elements: !15)
!14 = !DIBasicType(name: "char", size: 8, encoding: DW_ATE_signed_char)
!15 = !{!16}
!16 = !DISubrange(count: 100)
!17 = !DILocation(line: 11, column: 10, scope: !7)
!18 = !DILocalVariable(name: "mj", scope: !7, file: !1, line: 12, type: !10)
!19 = !DILocation(line: 12, column: 9, scope: !7)
!20 = !DILocation(line: 14, column: 5, scope: !7)
!21 = !DILocation(line: 15, column: 10, scope: !7)
!22 = !DILocation(line: 15, column: 5, scope: !7)
!23 = !DILocation(line: 17, column: 23, scope: !7)
!24 = !DILocation(line: 17, column: 10, scope: !7)
!25 = !DILocation(line: 17, column: 8, scope: !7)
!26 = !DILocation(line: 19, column: 60, scope: !7)
!27 = !DILocation(line: 19, column: 64, scope: !7)
!28 = !DILocation(line: 19, column: 5, scope: !7)
!29 = !DILocation(line: 20, column: 5, scope: !7)
!30 = !DILocation(line: 21, column: 5, scope: !7)
!31 = distinct !DISubprogram(name: "count_vowels", scope: !1, file: !1, line: 28, type: !32, isLocal: false, isDefinition: true, scopeLine: 29, flags: DIFlagPrototyped, isOptimized: false, unit: !0, variables: !2)
!32 = !DISubroutineType(types: !33)
!33 = !{!10, !34}
!34 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !14, size: 64)
!35 = !DILocalVariable(name: "adi", arg: 1, scope: !31, file: !1, line: 28, type: !34)
!36 = !DILocation(line: 28, column: 23, scope: !31)
!37 = !DILocalVariable(name: "count", scope: !31, file: !1, line: 30, type: !10)
!38 = !DILocation(line: 30, column: 9, scope: !31)
!39 = !DILocalVariable(name: "c", scope: !31, file: !1, line: 30, type: !10)
!40 = !DILocation(line: 30, column: 20, scope: !31)
!41 = !DILocalVariable(name: "flag", scope: !31, file: !1, line: 30, type: !10)
!42 = !DILocation(line: 30, column: 26, scope: !31)
!43 = !DILocation(line: 31, column: 20, scope: !31)
!44 = !DILocation(line: 31, column: 1, scope: !31)
!45 = !DILocalVariable(name: "d", scope: !31, file: !1, line: 32, type: !14)
!46 = !DILocation(line: 32, column: 10, scope: !31)
!47 = !DILocation(line: 33, column: 5, scope: !31)
!48 = distinct !{!48, !47, !49}
!49 = !DILocation(line: 50, column: 21, scope: !31)
!50 = !DILocation(line: 39, column: 13, scope: !51)
!51 = distinct !DILexicalBlock(scope: !31, file: !1, line: 34, column: 5)
!52 = !DILocation(line: 39, column: 17, scope: !51)
!53 = !DILocation(line: 39, column: 11, scope: !51)
!54 = !DILocation(line: 43, column: 28, scope: !51)
!55 = !DILocation(line: 43, column: 16, scope: !51)
!56 = !DILocation(line: 43, column: 14, scope: !51)
!57 = !DILocation(line: 45, column: 12, scope: !58)
!58 = distinct !DILexicalBlock(scope: !51, file: !1, line: 45, column: 12)
!59 = !DILocation(line: 45, column: 17, scope: !58)
!60 = !DILocation(line: 45, column: 12, scope: !51)
!61 = !DILocation(line: 47, column: 18, scope: !62)
!62 = distinct !DILexicalBlock(scope: !58, file: !1, line: 46, column: 9)
!63 = !DILocation(line: 48, column: 9, scope: !62)
!64 = !DILocation(line: 49, column: 10, scope: !51)
!65 = !DILocation(line: 50, column: 12, scope: !31)
!66 = !DILocation(line: 50, column: 14, scope: !31)
!67 = !DILocation(line: 50, column: 5, scope: !51)
!68 = !DILocation(line: 52, column: 12, scope: !31)
!69 = !DILocation(line: 52, column: 5, scope: !31)
!70 = distinct !DISubprogram(name: "check_vowel", scope: !1, file: !1, line: 55, type: !71, isLocal: false, isDefinition: true, scopeLine: 56, flags: DIFlagPrototyped, isOptimized: false, unit: !0, variables: !2)
!71 = !DISubroutineType(types: !72)
!72 = !{!10, !14}
!73 = !DILocalVariable(name: "ajj", arg: 1, scope: !70, file: !1, line: 55, type: !14)
!74 = !DILocation(line: 55, column: 22, scope: !70)
!75 = !DILocation(line: 57, column: 8, scope: !76)
!76 = distinct !DILexicalBlock(scope: !70, file: !1, line: 57, column: 8)
!77 = !DILocation(line: 57, column: 12, scope: !76)
!78 = !DILocation(line: 57, column: 19, scope: !76)
!79 = !DILocation(line: 57, column: 22, scope: !76)
!80 = !DILocation(line: 57, column: 26, scope: !76)
!81 = !DILocation(line: 57, column: 8, scope: !70)
!82 = !DILocation(line: 58, column: 15, scope: !76)
!83 = !DILocation(line: 58, column: 18, scope: !76)
!84 = !DILocation(line: 58, column: 23, scope: !76)
!85 = !DILocation(line: 58, column: 13, scope: !76)
!86 = !DILocation(line: 58, column: 9, scope: !76)
!87 = !DILocation(line: 61, column: 8, scope: !88)
!88 = distinct !DILexicalBlock(scope: !70, file: !1, line: 61, column: 8)
!89 = !DILocation(line: 61, column: 12, scope: !88)
!90 = !DILocation(line: 61, column: 19, scope: !88)
!91 = !DILocation(line: 61, column: 22, scope: !88)
!92 = !DILocation(line: 61, column: 26, scope: !88)
!93 = !DILocation(line: 61, column: 33, scope: !88)
!94 = !DILocation(line: 61, column: 36, scope: !88)
!95 = !DILocation(line: 61, column: 40, scope: !88)
!96 = !DILocation(line: 61, column: 47, scope: !88)
!97 = !DILocation(line: 61, column: 50, scope: !88)
!98 = !DILocation(line: 61, column: 54, scope: !88)
!99 = !DILocation(line: 61, column: 61, scope: !88)
!100 = !DILocation(line: 61, column: 64, scope: !88)
!101 = !DILocation(line: 61, column: 68, scope: !88)
!102 = !DILocation(line: 61, column: 8, scope: !70)
!103 = !DILocation(line: 62, column: 9, scope: !88)
!104 = !DILocation(line: 64, column: 5, scope: !70)
!105 = !DILocation(line: 65, column: 1, scope: !70)
