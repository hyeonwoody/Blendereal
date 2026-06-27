# Blendereal

Blender에서 Mesh Vertex 좌표를 추출하고
이를 콘솔 출력 또는 외부 시스템으로 확장 가능한 형태의 확장 도구.

## 🧑‍💻: Intro
❓ Problem : 블렌더와 언리얼 엔진 간의 Vertex 데이터를 주고받을 표준화된 방법이 없다 😮

❗ Idea : Vertex 정보를 별도의 서버에 저장한 뒤 언리얼에서 불러온다 🤔

💯 Solution : 레이어드 아키텍처 구조로 Vertex / Edge / Face 도메인을 독립적으로 관리 😁

</br>

## 🖥️: API Documentation


</br>

</br>

## 🧱: Structure
```
Presentation Layer 
├── Panel (UI) 
└── Operator (Controller) 
Domain Layer 
└── Vertex Service (Pure Logic) 
Infrastructure (Planned) 
├── gRPC Client 
└── Queue Worker
```
</br>

## 🛢️: Entity Relationship Diagram

</br>

 ## 🚀: Build & Run

### Requirements
- Blender 5.0.1 ~ 5.1.0 (Extension System)
- Python 3.11

### Option A. Install from Release (Recommended)
빌드 과정 없이 [Releases](https://github.com/hyeonwoody/blendereal-client/releases) 페이지에서 패키지를 받아 바로 설치합니다.

```
1. Releases에서 blendereal-1.0.0.zip 다운로드
2. Blender 실행 → Edit → Preferences → Get Extensions
3. 우측 상단 ▾ → Install from Disk... 클릭
4. 다운로드한 blendereal-1.0.0.zip 선택
5. Add-on 활성화 (체크박스)
```

### Option B. Build from source
직접 빌드하려면 저장소 루트에서 Blender의 Extension 빌드 명령으로 zip을 생성합니다.

```bash
# build.sh 사용 (Windows / Git Bash 기준)
./build.sh

# 또는 직접 실행
blender --command extension build
```

빌드가 완료되면 루트에 `blendereal-1.0.0.zip` 패키지가 생성됩니다. 이후 Option A의 2~5단계로 설치하세요.

> 💡 `build.sh`에는 Blender 실행 파일 경로가 하드코딩되어 있습니다.
> 설치 환경에 맞게 경로를 수정하거나, PATH에 등록된 `blender` 명령을 직접 사용하세요.

### Run
3D Viewport에서 패널을 열어 Mesh Vertex 좌표 추출 기능을 사용합니다.
</br>

## 🗓️: Development Period

<br>

## 🔥: Accomplishments

<br>

## ✅: Implementation

<br>

## 📓: Log

### 2026.04.09
Init project repository.


<br>

## 🎥: Demonstration

</br>

## 🎨: Design

</br>

## 📞: Contact
- 이메일: hyeonwoody@gmail.com
- 블로그: https://velog.io/@hyeonwoody
- 깃헙: https://github.com/hyeonwoody

</br>

## 🛠️: Technologies Used
> Python 3.11
> Blender 5.0+ Extension System
> BMesh API

</br>

## 📚: Libraries Used
> bpy (Blender Python API)
> bmesh

## 📖: Wiki

<br>
