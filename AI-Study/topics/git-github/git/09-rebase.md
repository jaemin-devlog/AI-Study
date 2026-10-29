# Rebase

커밋을 새 기준 뒤에 다시 적용. 작업 브랜치의 이력 재작성.

## main을 기준으로 다시 적용

대상은 `docs/git-note`의 미공유 커밋, 기준은 현재 로컬 `main`. 작업 폴더에 미커밋 변경 없음.

```powershell
git switch docs/git-note
git rebase main
```

![B에서 갈라진 D와 E를 C 뒤의 D-prime과 E-prime으로 재작성하고 main은 C에 유지하는 rebase 전후 그림](../assets/rebase.svg)

- `D`, `E`: 기존 작업 커밋
- `D'`, `E'`: 새 기준 `C` 뒤에 재적용한 커밋. 해시 변경
- `docs/git-note`는 `E'`로 이동. `main`은 `C` 유지

| 작업 | 이력을 다루는 방식 |
| --- | --- |
| Merge | 기존 커밋을 유지하며 이력 병합 |
| Rebase | 선택한 커밋을 새 기준 뒤에 다시 적용 |

다른 사람이 쓰는 공유 이력은 단독 Rebase 금지. 이미 받은 사람의 이력과 어긋날 수 있음.

## 충돌이 났을 때

모든 충돌 파일 수정·저장 → 스테이지 등록 → Rebase 계속.

```powershell
git add topics/git-github/README.md
git rebase --continue
```

- 다음 커밋에서도 충돌 발생 시 같은 과정 반복
- 편집기가 열리면 커밋 메시지 확인·저장 후 닫기

진행 중인 Rebase 취소, 시작 전 상태로 복구.

```powershell
git rebase --abort
```

## main에 반영

Rebase 후 `main`에 추가 커밋이 없으면 Fast-forward 가능.

```powershell
git switch main
git merge --ff-only docs/git-note
```

`--ff-only`: 브랜치 위치만 이동할 수 있을 때 병합. 이력이 다시 갈라졌다면 중단.

참고: [Git rebase](https://git-scm.com/docs/git-rebase) · [Git merge](https://git-scm.com/docs/git-merge)

[목차로](../README.md)
