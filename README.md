# 実験数学C

## これは何?

2022年度第3ターム開講「実験数学C」の講義内で紹介したJupyter NotebookおよびPythonファイルをまとめている．

## 使い方 (2022/11/07現在)

※自身のコンピュータ (ローカル環境) を汚したくない人はこの節をスキップし，次節の [【発展】仮想環境のすゝめ]() に従ってください．

以下のコマンドを実行し，PowerShellからコマンドを実行する許可を与える：

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```

### Anacondaを使っている場合

(cf. [【Anacondaの使い方】よく使うcondaコマンド一覧【チートシート】/パッケージの管理](https://hogelog.com/python/conda-command.html#toc7))

`conda` コマンドを利用してモジュールを管理する．

1. Anaconda Promptを起動する．

2. 以下のコマンドを実行し，必要なパッケージレポジトリを追加する：

```terminal
conda config --add channels conda-forge
```

3. 以下のコマンドを実行し，必要な外部モジュールをインストールする：

```terminal
conda install ipykernel matplotlib nptyping numpy scipy sympy
```

### それ以外の場合

(cf. [Python環境構築ガイド/Windows環境のPython/pip](https://www.python.jp/install/windows/pip.html))

`pip` コマンドを利用してモジュールを管理する．

1. Powershell (またはWindows Terminal) を起動する．

2. 以下のコマンドを実行し，必要な外部モジュールをインストールする：

```powershell
python -m pip install "ipykernel>=6.17.0" "matplotlib>=3.6.2" "nptyping>=2.3.1" "numpy>=1.23.4" "scipy>=1.9.3" "sympy>=1.11.1"
```

## 【発展】仮想環境のすゝめ

### Anacondaを使っている場合

(cf. [Python環境構築ガイド/Anacondaのインストール/Conda コマンド](https://www.python.jp/install/anaconda/conda.html))

`conda` コマンドを利用してConda環境を管理する．

1. Anaconda Promptを起動する．

2. 以下のコマンドを実行し，Conda環境を作成する (\``emc''は\``2022 Experimental Mathematics C''の略です)：

```terminal
conda create --name 2022emc python=3.10
```

3. 以下のコマンドを実行し，Conda環境に入る：

```terminal
conda activate 2022emc
```

4. 以下のコマンドを実行し，必要な外部モジュールをインストールする：

```terminal
conda install ipykernel matplotlib nptyping numpy scipy sympy
```

### それ以外の場合

(cf. [Python環境構築ガイド/Windows環境のPython/仮想環境](https://www.python.jp/install/windows/venv.html))

venvを利用して仮想環境を管理する．

1. Powershell (またはWindows Terminal) を起動する．

2. 以下のコマンドを実行し，仮想環境を作成する：

```powershell
python -m venv .venv
```

3. 以下のコマンドの**いずれか**を実行し，仮想環境に入る：

- Windowsの場合

```powershell
.venv\Scripts\activate.ps1
```

- Linux (またはWSL) の場合

```bash
source .venv/bin/activate
```

4. 以下のコマンドを実行し，必要な外部モジュールをインストールする：

```powershell
python -m pip install "ipykernel>=6.17.0" "matplotlib>=3.6.2" "nptyping>=2.3.1" "numpy>=1.23.4" "scipy>=1.9.3" "sympy>=1.11.1"
```
