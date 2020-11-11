SELECT 
    CXC.ID_TERC AS codcli, 
    CXC.ID_TIPO_CRU AS tdoc, 
    CXC.ID_NRO_CRU AS ndoc, 
    '' AS nvcto, /* Validar con condicion de pago - relacionar plazos de pago */
    CXC.ID_FECHA_CONTAB AS fchemi, 
    CXC.ID_FECHA_VCTO AS fcvcto, 
    CXC.SALDOS_TOT_CARTERA AS importe, 
    0 AS estado, 
    0 AS dotada, 
    CXC.FORMA_PAGO_DOC AS codvp, 
    '' AS codcondp, 
    'COP' AS codmondoc, 
    '' AS impmondoc, 
    CXC.ID_CUENTA AS ind1, 
    '' AS ind2, 
    '' AS ind3, 
    '' AS ind4, 
    '' AS ind5, 
    '' AS ind6, 
    '' AS ind7, 
    '' AS ind8, 
    '' AS ind9, 
    CONCAT_WS('@#', CXC.ID_FECHA_CONTAB, CXC.ID_TIPO_CRU, CXC.ID_NRO_CRU) AS campoid, 
    '' AS codejercicio, 
    '' AS numdocorigen 

FROM 
    cgresumen_cxc AS CXC 
    INNER JOIN terceros AS T ON CXC.ID_TERC = T.CODIGO AND CXC.ID_SUC = T.SUCURSAL 
    INNER JOIN cuentas_contab AS CC ON CXC.ID_CUENTA = CC.CODIGO 
WHERE 
    CXC.ID_EMP = '{0}' 
    AND CXC.ID_FECHA_CANC = 0 
    AND CXC.LAPSO_DOC =  (SELECT MAX(LAPSO_DOC) FROM CGRESUMEN_CXC)
ORDER BY 
    T.CODIGO,
    CXC.ID_TIPO_CRU,
    CXC.ID_NRO_CRU,
    CXC.LAPSO_DOC
    ;