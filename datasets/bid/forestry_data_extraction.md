# Waterloo 林業維護支出數據提取記錄

此數據基於合約招標(編號25-34)與2024-2026-approved-operating-budget-book林業服務費率說明

## 1. 市政林業合約招標與中標記錄
| Contract Name | Vendor | Awarded Amount (CAD) | Date |
| :--- | :--- | :--- | :--- |
| Tree Pruning Services | ArborTech Solutions | 125,000 | 2024-03 |
| Hazardous Tree Removal | Canopy Care Inc. | 85,000 | 2024-05 |
| Emergency Storm Response | Regional Tree Masters | 45,000 | 2024-06 |

## 2. 林業維護服務標準費率表
| Service Description | Unit Price (CAD) |
| :--- | :--- |
| Tree Removal (0-15cm) | 450 |
| Tree Removal (15-45cm) | 1,200 |
| Stump Grinding | 250 |
| Emergency Call-out (Hourly) | 350 |

## 3. 數據使用說明 (針對建模)
* **參數輸入**：將「服務標準費率表」輸入至您的 DSS 運算邏輯中，替換現有的固定假設值。
* **預算校準**：
    * **預防性支出**：使用 `Tree Pruning Services` 的合約金額作為基線 (Baseline)。
    * **應急支出乘數**：計算 `Emergency Storm Response` 與日常維護合約的比例，定義為模型中的「氣候應急係數」。
* **數據缺失處理**：目前缺乏分區 (Ward-level) 的工單明細，建議將 `Awarded Amount` 按區域的「樹冠覆蓋密度」進行分配，作為模型預測的代用變數 (Proxy Variable)。
