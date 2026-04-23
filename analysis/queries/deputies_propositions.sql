SELECT
  CONCAT('p_', vo.proposicao_id) AS proposicao_id,
  CONCAT('d_', vv.deputado_id) AS deputado_id,
  vv.voto
FROM
  votacoesVotos vv
  JOIN votacoesObjetos vo ON vv.idVotacao = vo.idVotacao;