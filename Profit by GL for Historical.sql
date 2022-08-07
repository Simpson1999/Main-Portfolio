DECLARE
@StartDate Date='2021'
,@EndDate Date='2022'
;

WITH MaxInventoryHistory
AS
(
select
InventoryID
,MAX(InventoryHistoryID) as InventoryHistoryID
from Inventory_History IH
WHERE InventoryStatusID IN (3,4) and CustomerID is not null
Group By InventoryID
)

SELECT
cp.CompanyName 
,glj.GLAccount
,glj.PostDate
--,jv.InventoryId
,SUM(glj.amount) AS Amount
,case when glj.GLAccount in ('001-4113-0120','001-4113-0131','001-4113-0132','001-4112-0120','001-4112-0131','001-4112-0132','001-4110-0120','001-4110-0131','001-4110-0132') then 'Depreciation' 
when glj.GLAccount in ('001-3175-0120','001-4100-0120') then 'Sales Type Gain' 
when glj.GLAccount ='001-3121-0120' then 'Late Fee Revenue'
when glj.GLAccount in ('001-3212-0120','001-3212-0132') then 'Interim Interest'
when glj.GLAccount in ('001-3129-0120','001-3129-0131','001-3129-0132') then 'Interim Rent'
when glj.GLAccount ='001-3200-0120' then 'Registration Services'
when glj.GLAccount ='001-6123-0120' then 'Commission'
else 'Lease Revenue' end as [Type] 
FROM
GLJournalView glj
inner join MaxInventoryHistory on MaxInventoryHistory.InventoryID = glj.InventoryId
inner join Inventory_History IH on MaxInventoryHistory.InventoryId = IH.InventoryID and MaxInventoryHistory.InventoryHistoryID = IH.InventoryHistoryID
left join Customer_Profile CP on IH.CustomerID = CP.CustomerID 
	and AccountNumber not like 'B%' --hack to remove buyer accounts that somehow got assigned to lease/inventory assets
where glj.GLAccount in ('001-3150-0131','001-3150-0132','001-3150-0120','001-6123-0120','001-3143-0120','001-3144-0120','001-3145-0120','001-3146-0120','001-3147-0120','001-3148-0120','001-3139-0120','001-3137-0120','001-3135-0120','001-3133-0120','001-3131-0120','001-3140-0120','001-3138-0120','001-3136-0120','001-3134-0120','001-3132-0120','001-3130-0120','001-3143-0131','001-3144-0131','001-3145-0131','001-3146-0131','001-3147-0131','001-3148-0131','001-3139-0131','001-3137-0131','001-3135-0131','001-3133-0131','001-3131-0131','001-3140-0131','001-3138-0131','001-3136-0131','001-3134-0131','001-3132-0131','001-3130-0131','001-3143-0132','001-3144-0132','001-3145-0132','001-3146-0132','001-3147-0132','001-3148-0132','001-3139-0132','001-3137-0132','001-3135-0132','001-3133-0132','001-3131-0132','001-3140-0132','001-3138-0132','001-3136-0132','001-3134-0132','001-3132-0132','001-3130-0132'
,'001-3200-0120','001-3129-0132','001-3129-0131','001-3129-0120','001-3212-0132','001-3212-0120','001-3142-0131','001-3142-0132','001-3142-0120','001-3141-0120','001-3121-0120','001-3186-0120','001-4113-0120','001-4113-0131','001-4113-0132','001-4112-0120','001-4112-0131','001-4112-0132','001-3175-0120','001-4100-0120','001-4110-0120','001-4110-0131','001-4110-0132') and glj.PostDate>=@StartDate and glj.PostDate<=@EndDate
group by glj.GLAccount,CP.CompanyName,glj.PostDate
order by 1


/*
select
glj.GLAccount
,sum(glj.Amount) as Amount
,cp.CompanyName
from GLJournalView glj
inner join Inventory_Profile inp on glj.InventoryId=inp.InventoryID
inner join Customer_Profile cp on inp.CustomerID=cp.CustomerID
where glj.GLAccount in ('001-3201-0124') and glj.PostDate>=@StartDate and glj.PostDate<=@EndDate
group by glj.GLAccount,cp.CompanyName
*/


--select count(*) from GLJournalView where GLAccount in ('001-3201-0124') and PostDate>=@StartDate and PostDate<=@EndDate
