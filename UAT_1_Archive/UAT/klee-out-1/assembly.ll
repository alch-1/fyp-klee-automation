; ModuleID = 'uat_test2_annotated.bc'
source_filename = "uat_test2_annotated.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%struct.game = type { [50 x i8], i32 }

@.str = private unnamed_addr constant [2 x i8] c"g\00", align 1
@.str.1 = private unnamed_addr constant [8 x i8] c"Cricket\00", align 1
@.str.2 = private unnamed_addr constant [18 x i8] c"Name of game: %s\0A\00", align 1
@.str.3 = private unnamed_addr constant [23 x i8] c"Number of players: %d\0A\00", align 1

; Function Attrs: noinline nounwind uwtable
define i32 @main() #0 !dbg !7 {
entry:
  %retval = alloca i32, align 4
  %g = alloca %struct.game, align 4
  store i32 0, i32* %retval, align 4
  call void @llvm.dbg.declare(metadata %struct.game* %g, metadata !11, metadata !DIExpression()), !dbg !20
  %0 = bitcast %struct.game* %g to i8*, !dbg !21
  call void @klee_make_symbolic(i8* %0, i64 56, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str, i32 0, i32 0)), !dbg !22
  %game_name = getelementptr inbounds %struct.game, %struct.game* %g, i32 0, i32 0, !dbg !23
  %arraydecay = getelementptr inbounds [50 x i8], [50 x i8]* %game_name, i32 0, i32 0, !dbg !24
  %call = call i8* @strcpy(i8* %arraydecay, i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.1, i32 0, i32 0)) #4, !dbg !25
  %number_of_players = getelementptr inbounds %struct.game, %struct.game* %g, i32 0, i32 1, !dbg !26
  store i32 11, i32* %number_of_players, align 4, !dbg !27
  %game_name1 = getelementptr inbounds %struct.game, %struct.game* %g, i32 0, i32 0, !dbg !28
  %arraydecay2 = getelementptr inbounds [50 x i8], [50 x i8]* %game_name1, i32 0, i32 0, !dbg !29
  %call3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([18 x i8], [18 x i8]* @.str.2, i32 0, i32 0), i8* %arraydecay2), !dbg !30
  %number_of_players4 = getelementptr inbounds %struct.game, %struct.game* %g, i32 0, i32 1, !dbg !31
  %1 = load i32, i32* %number_of_players4, align 4, !dbg !31
  %call5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([23 x i8], [23 x i8]* @.str.3, i32 0, i32 0), i32 %1), !dbg !32
  ret i32 0, !dbg !33
}

; Function Attrs: nounwind readnone speculatable
declare void @llvm.dbg.declare(metadata, metadata, metadata) #1

declare void @klee_make_symbolic(i8*, i64, i8*) #2

; Function Attrs: nounwind
declare i8* @strcpy(i8*, i8*) #3

declare i32 @printf(i8*, ...) #2

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind readnone speculatable }
attributes #2 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #4 = { nounwind }

!llvm.dbg.cu = !{!0}
!llvm.module.flags = !{!3, !4, !5}
!llvm.ident = !{!6}

!0 = distinct !DICompileUnit(language: DW_LANG_C99, file: !1, producer: "clang version 6.0.1 ", isOptimized: false, runtimeVersion: 0, emissionKind: FullDebug, enums: !2)
!1 = !DIFile(filename: "uat_test2_annotated.c", directory: "/home/klee/FYP/FYP/UAT")
!2 = !{}
!3 = !{i32 2, !"Dwarf Version", i32 4}
!4 = !{i32 2, !"Debug Info Version", i32 3}
!5 = !{i32 1, !"wchar_size", i32 4}
!6 = !{!"clang version 6.0.1 "}
!7 = distinct !DISubprogram(name: "main", scope: !1, file: !1, line: 10, type: !8, isLocal: false, isDefinition: true, scopeLine: 11, isOptimized: false, unit: !0, variables: !2)
!8 = !DISubroutineType(types: !9)
!9 = !{!10}
!10 = !DIBasicType(name: "int", size: 32, encoding: DW_ATE_signed)
!11 = !DILocalVariable(name: "g", scope: !7, file: !1, line: 12, type: !12)
!12 = distinct !DICompositeType(tag: DW_TAG_structure_type, name: "game", file: !1, line: 4, size: 448, elements: !13)
!13 = !{!14, !19}
!14 = !DIDerivedType(tag: DW_TAG_member, name: "game_name", scope: !12, file: !1, line: 6, baseType: !15, size: 400)
!15 = !DICompositeType(tag: DW_TAG_array_type, baseType: !16, size: 400, elements: !17)
!16 = !DIBasicType(name: "char", size: 8, encoding: DW_ATE_signed_char)
!17 = !{!18}
!18 = !DISubrange(count: 50)
!19 = !DIDerivedType(tag: DW_TAG_member, name: "number_of_players", scope: !12, file: !1, line: 7, baseType: !10, size: 32, offset: 416)
!20 = !DILocation(line: 12, column: 15, scope: !7)
!21 = !DILocation(line: 13, column: 20, scope: !7)
!22 = !DILocation(line: 13, column: 1, scope: !7)
!23 = !DILocation(line: 15, column: 12, scope: !7)
!24 = !DILocation(line: 15, column: 10, scope: !7)
!25 = !DILocation(line: 15, column: 3, scope: !7)
!26 = !DILocation(line: 16, column: 5, scope: !7)
!27 = !DILocation(line: 16, column: 23, scope: !7)
!28 = !DILocation(line: 18, column: 34, scope: !7)
!29 = !DILocation(line: 18, column: 32, scope: !7)
!30 = !DILocation(line: 18, column: 3, scope: !7)
!31 = !DILocation(line: 19, column: 39, scope: !7)
!32 = !DILocation(line: 19, column: 3, scope: !7)
!33 = !DILocation(line: 21, column: 3, scope: !7)
