# TEST_CASES

## Case 1 - 左轉基本

- 輸入：初始 (1,1,N)，指令 L
- 預期結果：(1,1,W)，未 LOST
- 實際結果：(1,1,W)，未 LOST
- PASS/FAIL：PASS
- 對應測試函式：test_turn_left_from_north_is_west

## Case 2 - 右轉基本

- 輸入：初始 (1,1,N)，指令 R
- 預期結果：(1,1,E)，未 LOST
- 實際結果：(1,1,E)，未 LOST
- PASS/FAIL：PASS
- 對應測試函式：test_turn_right_from_north_is_east

## Case 3 - 連續旋轉

- 輸入：初始 (1,1,N)，指令 RRRR
- 預期結果：方向回到 N
- 實際結果：方向回到 N
- PASS/FAIL：PASS
- 對應測試函式：test_four_right_turns_return_to_original_direction

## Case 4 - 邊界內前進

- 輸入：初始 (1,1,N)，指令 F
- 預期結果：(1,2,N)，未 LOST
- 實際結果：(1,2,N)，未 LOST
- PASS/FAIL：PASS
- 對應測試函式：test_forward_inside_boundary_is_safe

## Case 5 - 邊界外前進會 LOST

- 輸入：初始 (0,3,N)，指令 F
- 預期結果：停在 (0,3,N)，LOST=True
- 實際結果：停在 (0,3,N)，LOST=True
- PASS/FAIL：PASS
- 對應測試函式：test_forward_out_of_boundary_causes_lost

## Case 6 - LOST 後停止執行

- 輸入：初始 (0,3,N)，指令 FRF
- 預期結果：第一步 LOST 後不再執行 R/F
- 實際結果：狀態維持 (0,3,N)，LOST=True
- PASS/FAIL：PASS
- 對應測試函式：test_lost_robot_stops_processing_remaining_commands

## Case 7 - 第一台越界留下 scent

- 輸入：初始 (3,3,N)，指令 F
- 預期結果：scent 包含 (3,3,N)
- 實際結果：scent 包含 (3,3,N)
- PASS/FAIL：PASS
- 對應測試函式：test_first_lost_robot_leaves_scent

## Case 8 - 第二台同格同向忽略危險 F

- 輸入：第一台在 (3,3,N) 執行 F 後 LOST，第二台同點同向執行 F
- 預期結果：第二台不移動、不 LOST
- 實際結果：第二台停在 (3,3,N)，LOST=False
- PASS/FAIL：PASS
- 對應測試函式：test_second_robot_ignores_dangerous_forward_when_scent_exists

## Case 9 - 同格不同方向不共用 scent

- 輸入：先留下 (3,3,N) scent，再以 (3,2,E) 執行 F
- 預期結果：可以前進到 (4,2,E)
- 實際結果：前進到 (4,2,E)
- PASS/FAIL：PASS
- 對應測試函式：test_same_cell_different_direction_does_not_share_scent

## Case 10 - 非法指令策略

- 輸入：初始 (1,1,N)，指令 X
- 預期結果：拋出 ValueError
- 實際結果：拋出 ValueError
- PASS/FAIL：PASS
- 對應測試函式：test_invalid_command_raises_value_error
