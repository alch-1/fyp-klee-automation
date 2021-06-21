; ModuleID = 'uat_test5_annotated.bc'
source_filename = "uat_test5_annotated.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str = private unnamed_addr constant [4 x i8] c"num\00", align 1
@.str.1 = private unnamed_addr constant [42 x i8] c"Enter any number to calculate factorial: \00", align 1
@.str.2 = private unnamed_addr constant [23 x i8] c"Factorial of %d = %llu\00", align 1

; Function Attrs: noinline nounwind uwtable
define i32 @main() #0 !dbg !7 {
entry:
  %retval = alloca i32, align 4
  %i = alloca i32, align 4
  %num = alloca i32, align 4
  %fact = alloca i64, align 8
  store i32 0, i32* %retval, align 4
  call void @llvm.dbg.declare(metadata i32* %i, metadata !11, metadata !DIExpression()), !dbg !12
  call void @llvm.dbg.declare(metadata i32* %num, metadata !13, metadata !DIExpression()), !dbg !14
  %0 = bitcast i32* %num to i8*, !dbg !15
  call void @klee_make_symbolic(i8* %0, i64 4, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str, i32 0, i32 0)), !dbg !16
  call void @llvm.dbg.declare(metadata i64* %fact, metadata !17, metadata !DIExpression()), !dbg !19
  store i64 1, i64* %fact, align 8, !dbg !19
  %call = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([42 x i8], [42 x i8]* @.str.1, i32 0, i32 0)), !dbg !20
  store i32 1, i32* %i, align 4, !dbg !21
  br label %for.cond, !dbg !23

for.cond:                                         ; preds = %for.body, %entry
  %1 = load i32, i32* %i, align 4, !dbg !24
  %2 = load i32, i32* %num, align 4, !dbg !26
  %cmp = icmp sle i32 %1, %2, !dbg !27
  br i1 %cmp, label %for.body, label %for.end, !dbg !28

for.body:                                         ; preds = %for.cond
  %3 = load i64, i64* %fact, align 8, !dbg !29
  %4 = load i32, i32* %i, align 4, !dbg !31
  %conv = sext i32 %4 to i64, !dbg !31
  %mul = mul i64 %3, %conv, !dbg !32
  store i64 %mul, i64* %fact, align 8, !dbg !33
  %5 = load i32, i32* %i, align 4, !dbg !34
  %inc = add nsw i32 %5, 1, !dbg !34
  store i32 %inc, i32* %i, align 4, !dbg !34
  br label %for.cond, !dbg !35, !llvm.loop !36

for.end:                                          ; preds = %for.cond
  %6 = load i32, i32* %num, align 4, !dbg !38
  %7 = load i64, i64* %fact, align 8, !dbg !39
  %call1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([23 x i8], [23 x i8]* @.str.2, i32 0, i32 0), i32 %6, i64 %7), !dbg !40
  ret i32 0, !dbg !41
}

; Function Attrs: nounwind readnone speculatable
declare void @llvm.dbg.declare(metadata, metadata, metadata) #1

declare void @klee_make_symbolic(i8*, i64, i8*) #2

declare i32 @printf(i8*, ...) #2

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind readnone speculatable }
attributes #2 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.dbg.cu = !{!0}
!llvm.module.flags = !{!3, !4, !5}
!llvm.ident = !{!6}

!0 = distinct !DICompileUnit(language: DW_LANG_C99, file: !1, producer: "clang version 6.0.1 ", isOptimized: false, runtimeVersion: 0, emissionKind: FullDebug, enums: !2)
!1 = !DIFile(filename: "uat_test5_annotated.c", directory: "/home/klee/FYP/clean_UAT/UAT")
!2 = !{}
!3 = !{i32 2, !"Dwarf Version", i32 4}
!4 = !{i32 2, !"Debug Info Version", i32 3}
!5 = !{i32 1, !"wchar_size", i32 4}
!6 = !{!"clang version 6.0.1 "}
!7 = distinct !DISubprogram(name: "main", scope: !1, file: !1, line: 4, type: !8, isLocal: false, isDefinition: true, scopeLine: 5, isOptimized: false, unit: !0, variables: !2)
!8 = !DISubroutineType(types: !9)
!9 = !{!10}
!10 = !DIBasicType(name: "int", size: 32, encoding: DW_ATE_signed)
!11 = !DILocalVariable(name: "i", scope: !7, file: !1, line: 6, type: !10)
!12 = !DILocation(line: 6, column: 9, scope: !7)
!13 = !DILocalVariable(name: "num", scope: !7, file: !1, line: 6, type: !10)
!14 = !DILocation(line: 6, column: 12, scope: !7)
!15 = !DILocation(line: 7, column: 20, scope: !7)
!16 = !DILocation(line: 7, column: 1, scope: !7)
!17 = !DILocalVariable(name: "fact", scope: !7, file: !1, line: 8, type: !18)
!18 = !DIBasicType(name: "long long unsigned int", size: 64, encoding: DW_ATE_unsigned)
!19 = !DILocation(line: 8, column: 24, scope: !7)
!20 = !DILocation(line: 11, column: 5, scope: !7)
!21 = !DILocation(line: 15, column: 10, scope: !22)
!22 = distinct !DILexicalBlock(scope: !7, file: !1, line: 15, column: 5)
!23 = !DILocation(line: 15, column: 9, scope: !22)
!24 = !DILocation(line: 15, column: 14, scope: !25)
!25 = distinct !DILexicalBlock(scope: !22, file: !1, line: 15, column: 5)
!26 = !DILocation(line: 15, column: 17, scope: !25)
!27 = !DILocation(line: 15, column: 15, scope: !25)
!28 = !DILocation(line: 15, column: 5, scope: !22)
!29 = !DILocation(line: 17, column: 16, scope: !30)
!30 = distinct !DILexicalBlock(scope: !25, file: !1, line: 16, column: 5)
!31 = !DILocation(line: 17, column: 23, scope: !30)
!32 = !DILocation(line: 17, column: 21, scope: !30)
!33 = !DILocation(line: 17, column: 14, scope: !30)
!34 = !DILocation(line: 15, column: 23, scope: !25)
!35 = !DILocation(line: 15, column: 5, scope: !25)
!36 = distinct !{!36, !28, !37}
!37 = !DILocation(line: 18, column: 5, scope: !22)
!38 = !DILocation(line: 20, column: 38, scope: !7)
!39 = !DILocation(line: 20, column: 43, scope: !7)
!40 = !DILocation(line: 20, column: 5, scope: !7)
!41 = !DILocation(line: 22, column: 5, scope: !7)
