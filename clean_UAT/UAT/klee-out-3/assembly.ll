; ModuleID = 'uat_test4_annotated.bc'
source_filename = "uat_test4_annotated.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str = private unnamed_addr constant [8 x i8] c"number1\00", align 1
@.str.1 = private unnamed_addr constant [21 x i8] c"Enter two integers: \00", align 1
@.str.2 = private unnamed_addr constant [8 x i8] c"number2\00", align 1
@.str.3 = private unnamed_addr constant [13 x i8] c"%d + %d = %d\00", align 1

; Function Attrs: noinline nounwind uwtable
define i32 @main() #0 !dbg !7 {
entry:
  %retval = alloca i32, align 4
  %number1 = alloca i32, align 4
  %sum = alloca i32, align 4
  %number2 = alloca i32, align 4
  store i32 0, i32* %retval, align 4
  call void @llvm.dbg.declare(metadata i32* %number1, metadata !11, metadata !DIExpression()), !dbg !12
  call void @llvm.dbg.declare(metadata i32* %sum, metadata !13, metadata !DIExpression()), !dbg !14
  %0 = bitcast i32* %number1 to i8*, !dbg !15
  call void @klee_make_symbolic(i8* %0, i64 4, i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str, i32 0, i32 0)), !dbg !16
  %call = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([21 x i8], [21 x i8]* @.str.1, i32 0, i32 0)), !dbg !17
  call void @llvm.dbg.declare(metadata i32* %number2, metadata !18, metadata !DIExpression()), !dbg !19
  store i32 2, i32* %number2, align 4, !dbg !19
  %1 = bitcast i32* %number2 to i8*, !dbg !20
  call void @klee_make_symbolic(i8* %1, i64 4, i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.2, i32 0, i32 0)), !dbg !21
  %2 = load i32, i32* %number1, align 4, !dbg !22
  %3 = load i32, i32* %number2, align 4, !dbg !23
  %add = add nsw i32 %2, %3, !dbg !24
  store i32 %add, i32* %sum, align 4, !dbg !25
  %4 = load i32, i32* %number1, align 4, !dbg !26
  %5 = load i32, i32* %number2, align 4, !dbg !27
  %6 = load i32, i32* %sum, align 4, !dbg !28
  %call1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([13 x i8], [13 x i8]* @.str.3, i32 0, i32 0), i32 %4, i32 %5, i32 %6), !dbg !29
  ret i32 0, !dbg !30
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
!1 = !DIFile(filename: "uat_test4_annotated.c", directory: "/home/klee/FYP/clean_UAT/UAT")
!2 = !{}
!3 = !{i32 2, !"Dwarf Version", i32 4}
!4 = !{i32 2, !"Debug Info Version", i32 3}
!5 = !{i32 1, !"wchar_size", i32 4}
!6 = !{!"clang version 6.0.1 "}
!7 = distinct !DISubprogram(name: "main", scope: !1, file: !1, line: 4, type: !8, isLocal: false, isDefinition: true, scopeLine: 4, isOptimized: false, unit: !0, variables: !2)
!8 = !DISubroutineType(types: !9)
!9 = !{!10}
!10 = !DIBasicType(name: "int", size: 32, encoding: DW_ATE_signed)
!11 = !DILocalVariable(name: "number1", scope: !7, file: !1, line: 6, type: !10)
!12 = !DILocation(line: 6, column: 9, scope: !7)
!13 = !DILocalVariable(name: "sum", scope: !7, file: !1, line: 6, type: !10)
!14 = !DILocation(line: 6, column: 18, scope: !7)
!15 = !DILocation(line: 7, column: 20, scope: !7)
!16 = !DILocation(line: 7, column: 1, scope: !7)
!17 = !DILocation(line: 9, column: 5, scope: !7)
!18 = !DILocalVariable(name: "number2", scope: !7, file: !1, line: 11, type: !10)
!19 = !DILocation(line: 11, column: 9, scope: !7)
!20 = !DILocation(line: 12, column: 20, scope: !7)
!21 = !DILocation(line: 12, column: 1, scope: !7)
!22 = !DILocation(line: 14, column: 11, scope: !7)
!23 = !DILocation(line: 14, column: 21, scope: !7)
!24 = !DILocation(line: 14, column: 19, scope: !7)
!25 = !DILocation(line: 14, column: 9, scope: !7)
!26 = !DILocation(line: 16, column: 28, scope: !7)
!27 = !DILocation(line: 16, column: 37, scope: !7)
!28 = !DILocation(line: 16, column: 46, scope: !7)
!29 = !DILocation(line: 16, column: 5, scope: !7)
!30 = !DILocation(line: 17, column: 5, scope: !7)
